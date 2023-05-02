from django.db import models
import owlready2 as owl
# Create your views here.

# Create your models here.
class Ontology:
    def __init__(self) -> None:
        self.onto = owl.get_ontology("db/universite.owl").load()
        pass
    
    def getUniversite(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX : <http://www.semanticweb.org/ontologies/2021/1/universite#>
        SELECT *
            WHERE {
            ?s rdf:type :Universite ;
                :visionUniversite ?VisionUniversite;
                :logoUniversite ?logoUniversite;
                :descriptionUniversite ?descriptionUniversite;
                :nomUniversite ?nomUniversite;
                :missionUniversite ?missionUniversite;
                :contacteUniversite ?contactUniversite;
                :imageCouvertureUniversite ?imageCouvertureUniversite.
        }
        """
        results = list(owl.default_world.sparql(query))
        results = results[-1]
        
        
        site_query ="""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX : <http://www.semanticweb.org/ontologies/2021/1/universite#>
            SELECT ?nomsite
                WHERE {
                ?s rdf:type :Universite ;
                :repartir ?site.
                ?site :nomSite ?nomsite
                }
        """
        results_site = list(owl.default_world.sparql(site_query))
        list_site = [site[0] for site in results_site]
        context = {
            "VisionUniversite":results[1],
            "logoUniversite":results[2],
            "descriptionUniversite":results[3],
            "nomUniversite":results[4],
            "missionUniversite":results[5],
            "contactUniversite":results[6],
            "imageCouvertureUniversite":results[7],
            "site_univ" : list_site 
        }
        return context
    
    def getActualities(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX : <http://www.semanticweb.org/ontologies/2021/1/universite#>
        SELECT *
            WHERE { ?actualite rdf:type :ActualiteUniversite;
                            :descriptionActualite ?descriptionActualite;
                            :auteurActualite ?auteurActualite;
                            :imageActualite ?imageActualite;
                            :resumeActualite ?resumeActualite;
                            :intituleActualite ?intituleActualite.
                    }
            LIMIT 2
        """
        results = list(owl.default_world.sparql(query))
        actualities_queries = []
        for res in results:
            actualities_queries.append({
                "descriptionActualite":res[1],
                "auteurActualite":res[2],
                "imageActualite":res[3],
                "resumeActualite":res[4],
                "intituleActualite":res[5],
            })
            
        print(actualities_queries)
    
        return actualities_queries
    
    def getFormation(self):
        result = self.onto.search(individuals_of=owl.IRIS["http://www.semanticweb.org/ontologies/2021/1/universite#EtablissementUniversite"])
        print(result)
        return 
    
    def getPresident(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX : <http://www.semanticweb.org/ontologies/2021/1/universite#>
        SELECT ?nom ?prenom ?grade ?photo ?mots
            WHERE { :president :photoPersonnel ?photo;
            :nomPersonnel ?nom;
            :prenomPersonnel ?prenom;
            :motDuPresident ?mots;
            :gradePersonnel ?grade.
        }
        """
        results = list(owl.default_world.sparql(query))
        unique_result = results[-1]
        data = {
            'nom':unique_result[0],
            'prenom':unique_result[1],
            'grade':unique_result[2],
            'photo':unique_result[3],
            'mots_du_president':unique_result[4],
        }
        return data
    
    def getPartenaire(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX : <http://www.semanticweb.org/ontologies/2021/1/universite#>
        SELECT ?intitulePartenaire ?logo
            WHERE {
            ?partenaire rdf:type :PartenaireUniversite.
            ?partenaire :intitulePartenaire ?intitulePartenaire;
                :logoPartenaire ?logo;
        }
        """ 
        results = list(owl.default_world.sparql(query))
        all_partnaire = []
        for result in results:
            all_partnaire.append({
                'partenaire':result[0],
                'logo':result[1],
            })
        return all_partnaire
            
    def getEnseignant(self):
        query="""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX : <http://www.semanticweb.org/ontologies/2021/1/universite#>
            SELECT *
                WHERE { ?enseignant rdf:type :EnseignantUniversite;
                            :prenomPersonnel ?prenomPersonnel;
                            :nomPersonnel ?nomPersonnel;
                            :gradePersonnel ?gradePersonnel;
                            :photoPersonnel ?photo;
                            :etre ?etablissement.
                        ?etablissement :accronymeEtablissement ?accronymeEtablissement
            }
        """
        results = list(owl.default_world.sparql(query))
        print(results)
        all_enseignant = []
        for res in results:
            data = {
                "prenomPersonnel":res[1],
                "nomPersonnel":res[2],
                "gradePersonnel":res[3],
                "photoPersonnel":res[4],
                "etablissement":res[5],
                "accronymeEtablissement":res[6]
            }
            all_enseignant.append(data)
        return all_enseignant
    
    def getEtablissement(self):
        query = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX : <http://www.semanticweb.org/ontologies/2021/1/universite#>
            SELECT *
                WHERE {
                    ?etabl rdf:type :EtablissementUniversite ;
                    :accronymeEtablissement ?accronyme;
                    :logoEtablissement ?logo.
            }
        """
        results = list(owl.default_world.sparql(query))
        print(results)
        all_Etablissement = []
        for res in results:
            data = {
                "accronyme":res[1],
                "logo":res[2],
            }
            all_Etablissement.append(data)
        return all_Etablissement
        
        