Editorial/
R E S C I E N C E C ML Reproducibility Challenge 2021
KoustuvSinha1,2,ID,JesseDodge6,SashaLuccioni5,ID,JessicaZosaForde4,ID,SharathChandraRaparthy3,ID,
JoellePineau1,2,8,ID,andRobertStojnic7,8,ID
1SchoolofComputerScience,McGillUniversity,Montreal,Canada–2Mila-QuebecAIInstitute,Montreal,Canada–3Université
deMontréal,Canada–4BrownUniversity,USA–5AllenInstituteforAI,USA–6HuggingFace,USA–7PapersWithCode,USA–
8MetaAI,USAandCanada
Editedby
NicolasP.Rougier
## 1 Introduction
Reviewedby
AnonymousReviewers
Theimportanceofreproducibilityinsciencecannotbeoverstated. Itisoneofthekey
Received
mechanismsinplacetoenforcethehighstandardsofscientificdiscoveries,andakeyin19May2022
gredientforanimpactfulscientificdiscovery,allowingfuturepractitionerstobuildon
Published theshouldersofpriorwork.Reproduciblesciencealsopromotesopenandaccessiblere23May2022 search,allowingthescientificcommunitytoquicklyintegratenewfindingsandconvert
ideastopracticemoreseamlessly. Inthespiritofpromotingacultureofreproducible
DOI
scienceintheMachineLearningcommunity, wehavehostedthefifthiterationofthe
10.5281/zenodo.6574723
MLReproducibilityChallengein2021. Followingthetrendofinclusivityandbreadth,
this iteration involves a challenge to reproduce papers published in nine top conferencesinMachineLearning,includingNeurIPS,ICML,ICLR,CVPR,ICCV,ACL,EMNLP,
AAAI and IJCAI. An important objective of this challenge is to contribute toward improving the understanding of the central claims of the papers published in these top
conferences,byinvitingparticipantstorunreproducibilitystudyonthem. InthisspecialissueofReScienceCJournal,weareproudtopresentthepeer‐reviewedaccepted
papersofthe2021MLReproducibilityChallenge.
## 2 Challenge
Thegoalofthechallengewastoreproducethecentralclaimsofpaperspublishedintop
MachineLearningconferencesoftheyear. Participantswereinvitedtoworkoneither
allclaims, orpartialclaims, dependingonthecomplexityoftheproject. Participants
werealsofreetoreuseauthors’codewhenavailable,whilebeingencouragedtoexplore
beyondsimplyrunningthecodeprovidedtoverifyreproducibility. Unliketheprevious
challenge, in this iteration we removed the “Claim paper” step. This step, which was
previously used, involved participants pre‐registering which paper they wanted to reproduce,inordertoencourageearlycommitment,narrowdowntheclaimstheywish
toexploreinthepaper,andcoveringalargernumberofpapers. However,wereceived
feedbackthatthisstepwasnotusefulforparticipants,whichwasalsoreflectedbythe
lowpercentageofthenumberofreproducibilityreportssubmittedvspapersclaimed.
Removingthisstepalsoreducedthecomplexityofparticipatinginthechallenge.
As in the last iteration, participants were free to claim multiple papers, and multiple
teamscouldclaimthesamepaper. Inthisiteration,weobservedajumpofreproducibilityreportsubmissionsto102,comparedto82fromlastyear(Figure1). Reproducibility
Copyright©2022K.Sinhaetal.,releasedunderaCreativeCommonsAttribution4.0Internationallicense.
CorrespondenceshouldbeaddressedtoKoustuvSinha(koustuv.sinha@mail.mcgill.ca)
Theauthorshavedeclaredthatnocompetinginterestsexist.
ReScienceC8.2(#48)–Sinhaetal.2022 1


Growth of ML Reproducibility Challenge
ACL 2021
|     | Submitted Accepted |     | 5.1% |     |

NeurIPS 2021
| 125 |     |     | 5.1%      | ICML 2021 |

|     |     |     | ICCV 2021 | 28.2%     |
| 100 |     |     | 15.4%     |           |

IJCAI 2021
|                             |                      |         | 10.3%                                   | ICLR 2021 |

| 50                          |                      |         |                                         | 10.3%     |
|                             |                      |         | CVPR 2021                               | AAAI 2021 |
| 25                          |                      |         | 15.4%                                   | 10.3%     |
| 0 ICLR 2019                 | NeurIPS 2019 RC 2020 | RC 2021 |                                         |           |
| (a)GrowthofMLRCovertheyears |                      |         | (b)Distributionofreproducibilityreports |           |
submittedperconferenceinMLRC2021
Figure1.StatisticsoftheMLReproducibilityChallenge
reportswerespreadacrossallnineconferences, withmostpaperschosenfromICML
2021,andtheleastfromACL2021.Amajorityoftheparticipantswerestudentsusingthe
challengeasapartoftheirmachinelearningcoursesfromvariousinstitutionsaround
theworld,includingbutnotlimitedto: KTH(RoyalInstituteofTechnologyStockholm,
Sweden), Queen’s University (Ontario, Canada), Indian Institute of Technology (Gandhinagar, India), University of Amsterdam (Netherlands), University of Southern California, (USA), Indian Institute of Technology (Guwahati, India), Tsinghua University
(China),UniversityofLjubljana(Slovenia),UniversityofMichigan(USA),Universityof
Waterloo(Ontario,Canada),IstanbulTechnicalUniversity(Turkey),andEPFL(Switzerland).
Afterin‐depthpeerreview,inthisspecialissuewepresentthetop471acceptedreports,
selectedfrom102submissions,thusdrivinguptheacceptanceratefrom28%lastyear
to47%thisyear. Thisincreaseislargelyduetosignificantimprovementsinthequality
ofthereports&theirmethodology,whichisencouragingtosee.
| 3 Best Paper | Awards |     |     |     |

Startingthisyear, wearepresentingbestpaperawardstoafewselectreportstohighlighttheexcellentqualityall‐roundoftheirreproducibilitywork. Theselectioncriteria
consistedofvotesfromtheAreaChairs,basedonthereproducibilitymotivation,experimentaldepth,resultsbeyondtheoriginalpaper,ablationstudies,anddiscussion/recommendations. We believe the community will appreciate the strong reproducibility
efforts in each of these papers, which will improve the understanding of the original
publications,andinspireauthorstopromotebetterscienceintheirownwork.
### 3.1 BestPaperAward
• PiyushBagad,JesseMaas,PaulHilders,DanilodeGoede;ReproducibilityStudyof
“CounterfactualGenerativeNetworks”
### 3.2 OutstandingPaperAward
• Matija Teršek, Domen Vreš, Maša Kljun; Study of “Counterfactual Generative Net-
work”
• IanHardy;[RE]AnImplementationofFairRobustLearning
1Weaccepted48reports,butoneteamdidnotsubmittheircamerareadyversiontillthetimeofthepublicationofthiseditorial.
| ReScienceC8.2(#48)–Sinhaetal.2022 |     |     |     | 2   |

• GuillyKolkman,Makskulicki,JanAthmer,AlexLabro;Strategicclassificationmade
practical:reproduction
• Andrea Lombardo, Matteo Tafuro, Tin HadžiVeljković, Lasse Becker‐Czarnetzki;
Onthereproducibilityof”ExacerbatingAlgorithmicBiasthroughFairnessAttacks”
## 4 Platforms
This challenge is conducted with the support of PapersWithCode2 and OpenReview3.
PapersWithCodeisanopen,collaborativeplatformtodiscoverlatesttrendingmachine
learningresearchpaperswiththeircodebases,whichenablesrapidre‐usabilityandreproducibilityofpublishedworks. PapersWithCodeenabledthechallengeorganizersto
reachawideaudienceofstudentsandresearcherswhoparticipatedinthecompetition.
As was the case last year, OpenReview provided crucial logistic support by providing
anuniqueplatformtoclaimandsubmitreproducibilityreports. Aftersubmission,all
reportswentthroughathoroughpeerreviewprocessconsistingofhundredsofreviewersfromtheMachineLearningcommunity, andOpenReviewprovidedaneasy‐to‐use
platformformanagingreviewsandadministrativeprocesses. Finally,weusedapublic
Githubrepository4toperformthefinaleditorialprocessofconvertingacceptedpapers
intoReScienceformat,andtherebypublish48highqualityreportsinthisspecialissue.
## 5 Conclusion
ReproducibilityofcentralclaimsofpaperspublishedinMachineLearningconferences
hasbeenacenterofconsiderableattentionoverthepastseveralyears. Inrecentyears,
conferences such as NeurIPS, ICLR, AAAI, ICML, EMNLP have routinely included reproducibilityworkshopsandchallengestocultivatethecultureofreproduciblescience
inthecommunity. Severalconferenceshavealsointroducedcodesubmissionpolicies
and Reproducibility Checklists to further advance the cause and build momentum of
reproduciblescience. Wehopeourcontinuedendeavourofhostingannualchallenges
andpublishinghigh‐qualitypeer‐reviewedreproducibilityreportswillcontributemore
informationaboutexistingpublishedpapers,andhelpstrengthentheircorecontributionsintheprocess,whilealsopromotingopen,accessibleandsoundmachinelearning
research.
## 6 Acknowledgement
We thank the board and program committee of NeurIPS, ICML, ICLR, ACL, EMNLP,
CVPR,ICCV,AAAI and IJCAIfor partnering with us in this massiveinitiativeand supporting the challenge. We thank the OpenReview team (in particular Andrew McCallum, Parag Pachpute, Melisa Bok, Celeste Martinez Gomez, Pam Mandler and Mohit
Uniyal)fortheirconstantsupportinhostingandbuildingthecustomizedportalused
inourchallenge. WethankAnaLucic,MauritsBleekerandSamarthBhargavfortheir
feedbackonusingtheReproducibilityChallengeintheircourseatUniversityofAmsterdam. WethankRobertStojnic,RossTaylorandElvisSaraviafromPapersWithCodefor
hostingandsupportingthechallengealongwithitslogistics. WethanktheReScience
board (in particular Nicolas Rougier, Konrad Hinsen, Olivia Guest and Benoît Girard)
forpresentingtheacceptedreportsintheiresteemedjournal. Finally,wethankallof
2https://paperswithcode.com
3https://openreview.net/group?id=ML_Reproducibility_Challenge/2021/Fall/
4https://github.com/ReScience/MLRC
ReScienceC8.2(#48)–Sinhaetal.2022 3


ourparticipantswhodedicatedtimeandefforttoverifyresultsthatwerenottheirown,
tohelpstrengthenourunderstandingoftheconceptspresentedinthepapers.
## 7 Reviewers
Ourreviewersneedaspecialsectiondedicatedtothankthemfortheirtirelessefforts
in screening and providing valuable feedback to the Area Chairs (Jesse Dodge, Sasha
Luccioni, Jessica Zosa Forde, Sharath Chandra Raparthy and Koustuv Sinha) to select
the best papers. We were fortunate enough to attract a large pool of reviewers, who
spenttheirprecioustimetocriticallyreviewthereports. Wewouldliketospecifically
acknowledge our Emergency reviewers who responded to our call for help to review
some additional reports at the last minute. Starting this iteration, we also introduce
Outstanding Reviewer Award to select reviewers for their high quality and timely reviewsforthechallenge. TheselectioncriteriainvolvedvotesfromtheAreaChairsafter
carefulreviewofthereviewspostedinthechallenge. Wethankthereviewersfortheir
exceptionaleffortandhopetheywillcontinuetosupportusinfutureiterations.
### 7.1 OutstandingReviewers
| AlexGu            | KaranShah        | PascalLamblin           |

| CagriColtekin     | LeoMLahti        | PrithvijitChattopadhyay |
| DavidRau          | MaximeWabartha   | SamuelAlbanie           |
| DivyatMahajan     | MaxwellDCollins  | SunnieS.Y.Kim           |
| FrederikPaulNolte | OlgaIsupova      | TobiasUelwer            |
| KanikaMadan       | OlivierDelalleau | VarunSundar             |
### 7.2 AllReviewers
| AbhinavAgarwalla       | HannaSuominen      | MartinKlissarov     |

| AkshayRavindraKulkarni | HaoHe              | MatthewKyleSchlegel |
| AliHürriyetoğlu        | HarshaKokel        | MatthewRyanKrause   |
| AndreasRuttor          | HengFang           | MayurArvind         |
| AnimeshGupta           | JiangwenSun        | MelanieF.Pradier    |
| AnisZahedifard         | JieFu              | MikeChrzanowski     |
| BrentM.Berry           | JishnuJaykumarP    | MinjiaZhang         |
| ChaoQin                | KaushyKularatnam   | MonjoySaha          |
| DavidArbour            | KianaAlikhademi    | NadiaTahiri         |
| DavidKrueger           | LabibaKanijRupty   | NanRosemaryKe       |
| DongGong               | LiErranLi          | NikolaosVasiloglou  |
| FanFeng                | LluisCastrejon     | OtasowieOwolafe     |
| FelixGimeno            | MahimaAgumbeSuresh | OwenLockwood        |
| FurkanKınlı            | MahzadKhoshlessan  | PabloRobles‐Granda  |
| GabrielSynnaeve        | MajaSchneider      | PatrickPhilipp      |
| GangWang               | ManiA              | PaulTylkin          |
| GeorgiosLeontidis      | MarijaStanojevic   | PrateekGarg         |
ReScienceC8.2(#48)–Sinhaetal.2022 4


| PraveenNarayanan | StefanMagureanu | XiangZhang |

| QingzhiHu        | UjjwalVerma     |            |
XinLu
| RajGhugare | VenkatadheerajPichapati |     |

XinggangWang
| RameshRagala  | VibhaBelavadi |           |

| RazvanPascanu | WeiHan        | XingruiYu |
| SamiranDas    | WenbinZhang   |           |
YuntianDeng
| SeohyunKim | WenhaoYu |     |

ZahraAtashgahi
| ShijuSS        | XavierBouthillier |              |

| SimonKornblith | XavierSumba       | ZhourongChen |
ReScienceC8.2(#48)–Sinhaetal.2022 5

---
**Source PDF:** `01dddb70e640.pdf` (2022_01_article.pdf)  
**URL:** https://zenodo.org/record/6574723/files/article.pdf
