from datetime import date
from pydantic import BaseModel
from typing import Union

class Stock(BaseModel):
    siren: int
    nic: int
    siret: int
    statutDiffusionEtablissement: str
    dateCreationEtablissement: Union[str, date]
    trancheEffectifsEtablissement: int
    anneeEffectifsEtablissement: int
    activitePrincipaleRegistreMetiersEtablissement: str
    dateDernierTraitementEtablissement: str
    etablissementSiege: bool
    nombrePeriodesEtablissement: int
    complementAdresseEtablissement: str
    numeroVoieEtablissement: int
    indiceRepetitionEtablissement: str
    typeVoieEtablissement: str
    libelleVoieEtablissement: str
    codePostalEtablissement: int
    libelleCommuneEtablissement: str
    libelleCommuneEtrangerEtablissement: str
    distributionSpecialeEtablissement: str
    codeCommuneEtablissement: str
    codeCedexEtablissement: str
    libelleCedexEtablissement: str
    codePaysEtrangerEtablissement: str
    libellePaysEtrangerEtablissement: str
    complementAdresse2Etablissement: str
    numeroVoie2Etablissement: str
    indiceRepetition2Etablissement: str
    typeVoie2Etablissement: str
    libelleVoie2Etablissement: str
    codePostal2Etablissement: str
    libelleCommune2Etablissement: str
    libelleCommuneEtranger2Etablissement: str
    distributionSpeciale2Etablissement: str
    codeCommune2Etablissement: str
    codeCedex2Etablissement: str
    libelleCedex2Etablissement: str
    codePaysEtranger2Etablissement: str
    libellePaysEtranger2Etablissement: str
    dateDebut: Union[str, date]
    etatAdministratifEtablissement: str
    enseigne1Etablissement: str
    enseigne2Etablissement: str
    enseigne3Etablissement: str
    denominationUsuelleEtablissement: str
    activitePrincipaleEtablissement: str
    nomenclatureActivitePrincipaleEtablissement: str
    caractereEmployeurEtablissement: str
    libelleCommune2Etablissement: str