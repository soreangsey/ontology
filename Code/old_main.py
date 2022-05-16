from owlready2 import *


class SparqlQueries:
    def __init__(self):
        my_world = World()
        my_world.get_ontology("AgileOntology6_3_19.owl").load()  # path to the owl file is given here
        sync_reasoner(my_world, debug=1, infer_property_values=True,
                      keep_tmp_file=True)  # reasoner is started and synchronized here
        self.graph = my_world.as_rdflib_graph()

    def search(self):
        # Search query is given here
        # Base URL of your ontology has to be given here
        # query = "base <http://www.semanticweb.org/skiv/ontologies/2016/9/untitled-ontology-6#> " \
        #         "SELECT ?instance_x ?y " \
        #         "WHERE { " \
        #         "?instance_x rdf:type agile:Problem .lu " \
        #         "?instance_x agile:Caused_by ?y " \
        #         "filter( regex(str(?y), 'Daily_meeting' ))" \
        #         "}"
        query = '''PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX agile: <http://www.semanticweb.org/skiv/ontologies/2016/9/untitled-ontology-6#>
            SELECT DISTINCT  ?cause ?instance_x
           	WHERE {
                        ?instance_x rdf:type agile:Problem.
            		?practice rdf:type agile:Practice.
           	 	?practice agile:Encounter ?instance_x.
           	 	
            		?cause rdf:type agile:Situation.
            		?Team rdf:type agile:Team.
            	    
            		?team agile:Have ?cause.
            		?cause agile:Cause ?instance_x.
            		FILTER( regex(str(?practice), "Daily"))
            		FILTER (regex(str(?team),"Test"))}
           

        '''

        # query is being run
        # resultsList = self.graph.query(query)
        resultsList = self.graph.query_owlready(query)

        nb = 0
        # creating json object
        response = list(resultsList)
        print(len(response))

        response = [[str(e) for e in each] for each in response]
        for each in response:
            print(each[0], each[1])
        print('nb of response:', len(response))
        return response


if __name__ == '__main__':
    runQuery = SparqlQueries()
    runQuery.search()
