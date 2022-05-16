# -*- coding: utf-8 -*-
from owlready2 import *


class SparqlQueries:
    def __init__(self):
        # owlready2.JAVA_EXE = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Java\java.exe"

        situationList = ["Situation:Experience_in_techonology_knowledge", "Situation:no_agile_experience",
                         "Situation:2_years_agile_experience", "Situation:Distributed_Team",
                         "Situation:User_hardly_available",
                         "Situation:Virtual_communication", "Situation:No_domain_knowledge"]
        goalList = ["Goal:Gradual_transfer_of_responsibilities_from_project_manager_to_development_team",
                    "Goal:Enhanced_Project_Visibility"]
        practiceList = ["Daily_meeting", "Short_iteration"]
        my_world = World()
        myOnto = my_world.get_ontology("AgileOntology9_4_19.owl").load()  # path to the owl file is given here

        tmpTeam = myOnto.Team("Tmp_team")
        for i in range(len(situationList)):
            situation = myOnto.Situation(situationList[i])
            tmpTeam.Have.append(situation)
        for i in range(len(goalList)):
            goal = myOnto.Goal(goalList[i])
            tmpTeam.Have.append(goal)
        for i in range(len(practiceList)):
            practice = myOnto.Practice(practiceList[i])
            tmpTeam.Adopt.append(practice)
        print(tmpTeam)

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
        #         "}"x
        query = u'''PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX agile: <http://www.semanticweb.org/skiv/ontologies/2016/9/untitled-ontology-6#>
            
            SELECT DISTINCT ?team ?instance_x
            WHERE { 
            ?team rdf:type agile:Team.
            ?team agile:Achieve ?instance_x.
            ?instance_x rdf:type agile:Goal.
            FILTER( regex(str(?team), "Tmp"))}
            



        '''

        # the one that doesnt work

        # query = "base <http://www.semanticweb.org/skiv/ontologies/2016/9/untitled-ontology-6#> " \
        #         "SELECT ?s ?p ?o " \
        #         "WHERE { " \
        #         "?s ?p ?o . " \
        #         "}"

        # query is being run
        resultsList = self.graph.query(query)
        print(len(resultsList))
        # creating json object
        response = []
        for item in resultsList:
            s = str(item['instance_x'].toPython())
            s = re.sub(r'.*#', "", s)

            p = str(item['team'].toPython())
            p = re.sub(r'.*#', "", p)

            response.append({'s': s, 'p': p})

        print(response)  # just to show the output
        return response


if __name__ == '__main__':
    runQuery = SparqlQueries()
    runQuery.search()
