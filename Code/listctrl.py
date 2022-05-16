# encoding: utf-8
"""
List view widgets.
"""

from __future__ import absolute_import

from bisect import bisect
from collections import MutableSequence

import wx

__all__ = [
    'ColumnInfo',
    'ListCtrlUtil',
    'ListCtrlAutoWidthMixin',
    'ListCtrl',
    'EditListCtrl',
]


class ColumnInfo(object):

    def __init__(self, title, gettext, format=wx.LIST_FORMAT_LEFT,
                 width=wx.LIST_AUTOSIZE):
        """
        :param str title: column title
        :param callable gettext: formatter function item -> str
        :param int format: format argument for InsertColumn
        :param int width: width argument for InsertColumn
        """
        self.title = title
        self.gettext = gettext
        self.format = format
        self.width = width


class ListCtrlUtil(object):
    """Utility to transform window coordinates to row/col and vice versa."""

    def GetCellId(self, x, y):
        """Transform window (x, y) position to logical (row, col) coords."""
        row, flags = self.HitTest((x, y))
        col = bisect(self.col_locs, x + self.GetScrollPos(wx.HORIZONTAL)) - 1
        return row, col

    def ViewCellRect(self, row, col):

        """
        Scroll the specified cell into position if possible and return the
        (x0, y0, width, height) of the specified cell.
        """

        col_locs = self.col_locs
        x0 = col_locs[col]
        x1 = col_locs[col + 1]

        scrolloffset = self.GetScrollPos(wx.HORIZONTAL)

        # scroll forward
        if x1 - scrolloffset > self.GetSize()[0]:
            if wx.Platform == "__WXMSW__":
                # don't start scrolling unless we really need to
                offset = x1 - self.GetSize()[0] - scrolloffset
                # scroll a bit more than what is minimum required
                # so we don't have to scroll everytime the user presses TAB
                # which is very tireing to the eye
                addoffset = self.GetSize()[0] / 4
                # but be careful at the end of the list
                if addoffset + scrolloffset < self.GetSize()[0]:
                    offset += addoffset

                self.ScrollList(offset, 0)
                scrolloffset = self.GetScrollPos(wx.HORIZONTAL)
            else:
                # Since we can not programmatically scroll the ListCtrl
                # close the editor so the user can scroll and open the editor
                # again
                return None

        y0, _, height = self.GetItemRect(row)[1:]

        return (x0 - scrolloffset, y0, x1 - x0, height)

    @property
    def col_locs(self):
        """Starting positions (x coordinates) of each column."""
        # The column positions must be recomputed each time so adjustable
        # column widths are handled properly:
        col_locs = [0]
        loc = 0
        for n in range(self.GetColumnCount()):
            loc = loc + self.GetColumnWidth(n)
            col_locs.append(loc)
        return col_locs


class ListCtrlAutoWidthMixin:
    """
    A mix-in class that automatically resizes the columns in a wx.ListCtrl
    to fit their content + header label. If there is additional space left
    a specified column is resized to take up the remaining width.

    NOTE:    This only works for report-style lists.

    WARNING: If you override the EVT_SIZE event in your wx.ListCtrl, make
             sure you call event.Skip() to ensure that the mixin's _OnResize
             method is called.

    NOTE:    This class is different from the one written by Erik Westra
             which is distributed with wxPython and can be found in the module
             `wx.lib.mixins.listctrl` although its API and doc-strings are
             derived from that class.
    """

    def __init__(self, autosize_columns, resize_column=0):
        """Standard initialiser."""
        self._autosize_columns = autosize_columns
        self._resizeCol = 0
        self.Bind(wx.EVT_SIZE, self._onResize)

    def setResizeColumn(self, col):
        self._resizeCol = col

    def _onResize(self, event):
        """
        Respond to the wx.ListCtrl being resized.

        We automatically resize the last column in the list.
        """
        if 'gtk2' in wx.PlatformInfo or 'gtk3' in wx.PlatformInfo:
            self._doResize()
        else:
            wx.CallAfter(self._doResize)
        event.Skip()

    def _GetTextExtent(self, font, text):
        dc = wx.WindowDC(self)
        if font:
            dc.SetFont(font)
        return dc.GetTextExtent(text)

    def _GetMinItemExtent(self, row, col):
        item = self.GetItem(row, col)
        return self._GetTextExtent(item.GetFont(), item.GetText())

    def _HasHeader(self):
        return not (self.GetWindowStyle() & wx.LC_NO_HEADER)

    def _GetColTitle(self, col):
        return self.GetColumn(col).GetText()

    def _GetMinColWidth(self, col):
        if self.GetItemCount() > 0:
            w = max(self._GetMinItemExtent(row, col)[0]
                    for row in range(self.GetItemCount()))
        else:
            w = 0
        if self._HasHeader():
            title = self._GetColTitle(col)
            w = max(w, self._GetTextExtent(self.GetFont(), title)[0])
        return w + self.GetItemSpacing()[0]

    def _doResize(self):
        """
        Resize the last column as appropriate.

        If the list's columns are too wide to fit within the window, we use
        a horizontal scrollbar.  Otherwise, we expand the right-most column
        to take up the remaining free space in the list.

        We remember the current size of the last column, before resizing,
        as the preferred minimum width if we haven't previously been given
        or calculated a minimum width.  This ensure that repeated calls to
        _doResize() don't cause the last column to size itself too large.
        """

        if not self:  # avoid a PyDeadObject error
            return

        if self.GetSize().height < 32:
            return  # avoid an endless update bug when the height is small.

        numCols = self.GetColumnCount()
        if numCols == 0:
            return  # Nothing to resize.

        col_widths = [(self._GetMinColWidth(col)
                       if col in self._autosize_columns
                       else self.GetColumnWidth(col))
                      for col in range(numCols)]

        # We're showing the vertical scrollbar -> allow for scrollbar width
        # NOTE: on GTK, the scrollbar is included in the client size, but on
        # Windows it is not included
        listWidth = self.GetClientSize().width

        if sum(col_widths) < listWidth:
            col_widths[self._resizeCol] += listWidth - sum(col_widths)

        for col, width in enumerate(col_widths):
            self.SetColumnWidth(col, width)


class ListCtrlList(MutableSequence):
    """A list-like interface adapter for a wx.ListCtrl."""

    def __init__(self, ctrl, items):
        """Use the items object by reference."""
        self._items = items
        self._ctrl = ctrl

    # Sized

    def __len__(self):
        return len(self._items)

    # Iterable

    def __iter__(self):
        return iter(self._items)

    # Container

    def __contains__(self, value):
        return value in self._items

    # Sequence

    def __getitem__(self, index):
        return self._items[index]

    def __reversed__(self):
        return reversed(self._items)

    def index(self, value):
        return self._items.index(value)

    def count(self, value):
        return self._items.count(value)

    # MutableSequence

    def __setitem__(self, index, value):
        self._items[index] = value
        if isinstance(index, slice):
            self._refresh(0 if index.start is None else index.start,
                          -1 if index.stop is None else index.stop)
        else:
            self._refresh(index, index + 1)

    def __delitem__(self, index):
        del self._items[index]
        self._refresh(index, -1)

    def insert(self, index, value):
        self._items.insert(index, value)
        self._refresh(index, -1)

    append = MutableSequence.append

    def reverse(self):
        self._items.reverse()
        self._refresh(0, -1)

    def extend(self, values):
        old_len = len(self._items)
        self._items.extend(values)
        self._refresh(old_len, -1)

    pop = MutableSequence.pop
    remove = MutableSequence.remove
    __iadd__ = MutableSequence.__iadd__

    def _refresh(self, begin, end):
        count = len(self._items)
        self._ctrl.SetItemCount(count)
        if begin < 0:
            begin = max(0, begin + count)
        if end < 0:
            end += count + 1
        if end > begin:
            self._ctrl.RefreshItems(min(begin, count - 1),
                                    min(end - 1, count - 1))


class MyListCtrl(wx.ListCtrl, ListCtrlAutoWidthMixin, ListCtrlUtil):
    """
    ListCtrl that uses a list of :class:`ColumnInfo` to format its
    columns. The first column is auto-sized by default.
    """

    # TODO: support Ctrl-A + mouse selection
    # TODO: setter for selected_items/selected_indices

    def __init__(self, parent, id_, pos, size, style, columns):
        """
        Initialize list view.

        :param list columns: list of :class:`ColumnInfo`
        """
        # initialize super classes
        style |= wx.LC_REPORT
        wx.ListCtrl.__init__(self, parent, id_, pos, size, style=style)
        autosize_columns = [col for col, info in enumerate(columns)
                            if info.width == wx.LIST_AUTOSIZE]
        ListCtrlAutoWidthMixin.__init__(self, autosize_columns)
        # setup member variables
        self._items = ListCtrlList(self, [])
        self._columns = columns
        # insert columns
        for idx, col in enumerate(self._columns):
            self.InsertColumn(idx, col.title, col.format, col.width)

    @property
    def selected_items(self):
        """Iterate over all selected items."""
        return [self.items[idx] for idx in self.selected_indices]

    @property
    def selected_indices(self):
        """Iterate over all selected indices."""
        idx = self.GetFirstSelected()
        while idx != -1:
            yield idx
            idx = self.GetNextSelected(idx)

    @property
    def items(self):
        """Get list of data items."""
        return self._items

    @items.setter
    def items(self, items):
        """
        Update widget with new item list.

        :param list items: list of data items.
        """
        self._items[:] = items
        # TODO: keep the current selection if possible
        self._doResize()

    def OnGetItemText(self, row, col):
        """Get the text for the specified row/col."""
        return self._columns[col].gettext(self._items[row])

    # The following methods are usually only implemented by LC_VIRTUAL list
    # controls. We provide overrides that are useful for non-virtual controls
    # while maintaining the same API:

    def SetItemCount(self, count):
        for row in range(self.GetItemCount(), count):
            self.Append([""])
        for row in range(count, self.GetItemCount()):
            self.DeleteItem(row)

    def RefreshItems(self, start, end):
        for row in range(start, end + 1):
            for col in range(self.GetColumnCount()):
                text = unicode(self.OnGetItemText(row, col))
                self.SetStringItem(row, col, text)
