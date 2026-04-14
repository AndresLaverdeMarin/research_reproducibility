A&A492,657–673(2008) Astronomy
DOI:10.1051/0004-6361:200810685 &
(cid:2)c ESO2008 Astrophysics
Poincaré dodecahedral space parameter estimates
B.F.Roukema1,Z.Bulin´ski1,andN.E.Gaudin2
## 1 Torun´ CentreforAstronomy,NicolausCopernicusUniversity,ul.Gagarina11,87-100Torun´,Poland
e-mail:boud@astro.uni.torun.pl
2 ÉcolenationalesupérieuredephysiquedeStrasbourg,UniversitéLouisPasteur,Bd.SébastienBrant,BP10413,
67412IllkirchCedex,France
Received26July2008/Accepted25October2008
ABSTRACT
Context.Severalstudieshaveproposedthatthepreferredmodel ofthecomovingspatial3-hypersurface of theUniversemaybea
Poincarédodecahedralspace(PDS)ratherthanasimplyconnected,infinite,flatspace.
Aims.Here,weaimtoimprovethesurfaceoflastscattering(SLS)optimalcross-correlationmethodandapplythistoobservational
dataandsimulations.
Methods. Foragiven“generalised”PDSorientation,weanalyticallyderivetheformulaerequiredtoexcludepointsontheskythat
cannotbemembersofcloseSLS-SLScross-pairs.Theseenablemoreefficientpairselectionwithoutsacrificingtheuniformityofthe
underlyingselectionprocess.Forasufficientlysmallmatchedcirclesizeαandafixednumber ofrandomlyplacedpointsselected
foracross-correlationestimate,thecalculationtimeisdecreasedandthenumberofpairsperseparationbinisincreased.Usingthis
faster method, andincluding thesmallestseparation binwhen testingcorrelations, (i)werecalculateMonte CarloMarkov Chains
(MCMC)onthefive-yearWilkinsonMicrowaveAnisotropyProbe(WMAP)data;and(ii)weseekPDSsolutionsinasmallnumber
ofGaussianrandomfluctuation(GRF)simulationsinordertofurtherexplorethestatisticalsignificanceofthePDShypothesis.
Results.For5◦ <α<60◦,acalculationspeed-upof3–10isobtained.(i)ThebestestimatesofthePDSparametersforthefive-year
WMAPdataaresimilartothoseforthethree-yeardata;(ii)comparisonoftheoptimalsolutionsfoundbytheMCMCchainsinthe
observational maptothosefoundinthesimulatedmapsyieldsaslightlystrongerrejectionofthesimplyconnectedmodelusingα
ratherthanthetwistangleφ.Thebestestimateofαimpliesthat,givenalarge-scaleauto-correlationasweakasthatobserved,the
PDS-likecross-correlationsignalintheWMAPdataisexpectedwithaprobabilityoflessthanabout10%.Theexpecteddistribution
ofφfromtheGRFsimulationsisnotuniformon[−π,π].
Conclusions.Using this faster algorithm, we find that the previous PDS parameter estimates are stable to the update to five-year
WMAPdata.Moreover,foraninfinite,flat,cosmicconcordancemodelwithGaussianrandomfluctuations,thechanceoffindingboth
(a)alarge-scaleauto-correlationasweakasobserved;and(b)aPDS-likesignalsimilartowhatisobservedislessthanabout0.015%
to1.25%.
Keywords.cosmology:cosmologicalparameters–cosmology:observations–cosmology:theory
1. Introduction InRBSG08,themethodwasintroducedbypointingoutthat
algebraically, it is an extension of using the identified circles
During the past half-decade, attention has focussed on the principlefirstpublishedbyCornishetal.(1998).Here,wemake
Poincaré Dodecahedral Space (PDS) as a potentially better use of the fact that the cross-correlationmethod is not only an
modelof comovingspace than theinfinite flat model(Luminet algebraicextensionoftheidentifiedcirclesprinciple,butitsre-
et al. 2003; Roukema et al. 2004; Aurich et al. 2005a,b; lationtotheidentifiedcirclesprinciplecanalsobeinterpretedin
Gundermann 2005; Key et al. 2007; Niarchou & Jaffe 2007; termsofidentifiedannuli.Thisleadstoalgebraic/trigonometric
Caillerie et al. 2007; Lew & Roukema 2008; Roukema et al. relations that enable a faster calculation of cross-correlations,
2008).Ifthehypothesisthatthecomovingspatialsectionofthe withoutsacrificingtheuniformityoftheunderlyingrandomse-
Universeis a PDS is correct,thenit shouldbe possible to esti- lectionofpointsonthesky.Moreover,useoftheserelationsalso
mate the astronomicalcoordinatesof the fundamentaldomain, increasesthenumbersofpairsperseparationbin,leadingtoless
ashasbeentriedbyRoukemaetal.(2008,hereafter,RBSG08). relative Poisson noise in individualcross-correlationestimates.
Moreover,successive improvementsin data andanalysismeth- The annulusinterpretationand the associated relationsare pre-
ods should yield successively more precise and more accurate sentedinSect.3.1.
estimatesoftheseastronomicalcoordinates. In Sect. 3.2, use of this faster method to recalculate
Here, we aim to improve on the method of optimising the MonteCarlo MarkovChains(MCMC) forthe five-yearrelease
cross-correlation ξ (Eq. (1), RBSG08) of cosmic microwave oftheWMAPdataisdescribed.Sincethenewmethodincreases
C
background (CMB) temperature fluctuations between copies thenumbersofpairsperseparationbin,thesmallestseparation
of the surface of last scattering (SLS) presented in Roukema binavailablewhenestimatingcorrelationsshouldnotbeasnoisy
etal.(2008)andalsoappliedbyAurich(2008).We investigate aswithoutthisnewmethod,soweincludethissmallestsepara-
whether or not this can lead to improved parameter estimates. tionbin.
We also test a small number of simulations to see whether the Useofthisfastermethodalsomakesitpracticaltoperforma
infiniteflatmodelcanreproducetheobservationalsignal. consistentanalysisofboththeWMAPmapandasmallnumber
ArticlepublishedbyEDPSciences

658 B.F.Roukemaetal.:Poincarédodecahedralspaceparameters
ofGaussianrandomfluctuation(GRF)WMAPsimulatedmaps, forwhichEfstathiou(2004)findsthehighestprobabilityforthe
in order to estimate the expectationof a PDS-like signal under observed S value to occur in an infinite, flat, cosmic concor-
ξ
theassumptionofasimplyconnectedmodel.Inordertomodel dancemodel,soweshouldobtainaconservativeupperlimitto
this,weneedtoconsiderthefollowing. the probabilityof both(a)an S valueaslow asthatobserved;
ξ
One of the key motivationsfrom WMAP data for studying and (b) a PDS-like cross-correlation signal similar to that ob-
multiplyconnectedmodelshasbeenthelackofstructureonan- servedoccurring.ThisisdescribedinmoredetailinSect.3.3.
gularscaleslargerthanabout60◦,ashasbeennotedbyseveral
ResultsarepresentedinSect.4,discussedinSect.5andcon-
authors (e.g. Spergel et al. 2003; Luminet et al. 2003; Aurich clusionsaregiveninSect.6.Forgeneralbackgroundonspher-
etal.2005b).AswasnotedinRBSG08,inparticularinEq.(10), ical, multiply connected spaces, see Weeks (2001), Gausmann
ifthePDSmodelisincorrect,thencross-correlationsoftemper- et al. (2001),Lehoucqet al. (2002)and Riazuelo et al. (2004).
aturefluctuationsatpairsofpointsthatareimplied(bythePDS Seethereferencescitedaboveforbackgroundoncosmictopol-
hypothesis) to be spatially close should, on average, be much ogy.Comovingcoordinatesareusedwhendiscussingdistances
smallerthantheauto-correlationsatthesamesmallspatialsep- (i.e. “proper distances” at the present epoch, Weinberg 1972,
aration scale. This is because if the PDS model is wrong, then equivalent to “conformaltime” if c = 1) and the Hubble con-
thesepairsareinrealitywidelyseparatedratherthancloselysep- stantiswrittenH ≡100hkms−1Mpc−1.

arated,sotheircorrelationsshould,onaverage,besmall.
However,thisisonlyastatisticalstatement:evenforthecase
thatthePDSmodelisphysicallywrong,itispossiblethatsome 2. Observationsandsimulations
orientationsof a PDS model, by chance, happen to give cross-
2.1.Observations
correlationsthat violate Eq. (10) of RBSG08. How probableis
it for chance large-scale correlations in particular directions to
The analysis described in Sect. 3.2 uses the Internal Linear
mimic a PDS-like signal? This clearly depends on the ampli- Combination (ILC)1 all-sky map of the five-year WMAP data
tudeofthelargelength-scaleauto-correlation.Ifthisamplitude
(Hinshaw et al. 2009) and the foreground cleaned, Wiener
is low or high, then the chance of finding PDS-like signals us-
filtered version of the same five-year data published by the
ingtheoptimalcross-correlationmethodshouldbeloworhigh Tegmark et al. (2003) group (TOH)2 The “kp2” mask to elim-
respectively. Since the range of matched circle sizes α studied
inatetheGalacticPlaneandotherlikelycontaminatingregions,
in RBSG08 included circles with α ≤ 60◦, most of the cross-
coveringabout15%ofthesky,isusedthroughoutthispaperun-
correlations are from pairs of points separated observationally lessotherwisenoted3.Wedonotsmooththesemaps.
byangles(cid:2)60◦ ∼1rad.
The latter is the minimumscale abovewhich Spergelet al.
(2003) quantified the lack of temperature-temperature auto- 2.2.Simulationsandassociatedobservationalmap
correlations at large scales in the WMAP data, with their pa-
TheanalysisdescribedinSect.3.3usesaversionoftheWMAP
rameterS,defined
map andsky simulationspreparedconsistently fromthree-year
(cid:2)
1/2 observationalandsimulatedmapsintheQ,V andW frequency
S = [C(θ)]2dcosθ, (1) bands, weighted by inverse noise as given in Hinshaw et al.
−1 (2003),andsmoothedbyaGaussianofFWHM1◦,asdescribed
in Sect. 2 of Lew & Roukema (2008)4. Thisversionof the ob-
whereC(θ) is the two-pointauto-correlationfunctionat an an-
servationalmapisreferredtohereafteras“INC3”5.
gularseparationofθontheSLS(Sect.7,Eq.(9),Spergeletal.
As mentionedabove,the expectedvalue ofS fromthe in-
2003).Hereafter,wecallthisS ,inordertodistinguishitfrom ξ
ξ
finite, flat, cosmic concordance model is higher than that ob-
the S parameterused formatched circle analyses. The two pa-
rametershaveverydifferentmeanings. served.However,thereisa(small)chanceinthemodelthatsuch
alowS valueoccursinanysinglerealisationofthemodel,such
ThechanceofobservingS tobeassmallasthatobserved ξ
ξ as the one in which we live. Since we wish to test the chance
wasestimatedbySpergeletal.(2003)as0.15%foraninfinite,
that a PDS-like cross-correlationsignal occursgiven thatS is
flat, cosmic concordance model with a fixed spectral index of ξ
aslowasthatwhichisobserved,wegeneratesimulationsusing
densityperturbations.Efstathiou(2004),usingwhatshouldbea
theobservationalestimatesofthesphericalharmonicamplitudes
moreaccuratemethodifweassumeasimplyconnectedmodel,
C ofthetemperaturefluctuationsasestimatedinHinshawetal.
estimatedthechancestobemuchhigher,from3%to12.5%de- l
(2007), rather than using the mean values implied by an infi-
pendingonwhichskymapisanalysedandwhich(ifany)galac-
nite flat model.The phasesof the sphericalharmonicsare ran-
ticcutmaskisused(Table5,Efstathiou2004).
domised.Gaussiannoiseissimulatedaccordingtotheproperties
Wecanquantifytherelationbetweenlargelength-scaleauto-
andscanningstrategyofeachdifferencingassemblyandadded
correlationsandthechanceofaPDSsignalinthecasethatthe
toeachsimulatedmap.
PDSiswrongbywritingthatthelowertheobservedvalueofS ,
ξ
the less likely it is that a non-PDS model will give a PDS-like
1 http://lambda.gsfc.nasa.gov/data/map/dr3/dfp/
signal.Hence,sinceweexpectthatthetwoproperties,alowS
ξ wmap_ilc_5yr_v3.fits
value and a low chance of a PDS-like cross-correlation signal
2 http://space.mit.edu/home/tegmark/wmap/
occurring in a flat, infinite, cosmic concordancemodel, are re-
wiener5yr_map.fits
lated,itwouldnotbeusefultoestimatetheirprobabilitiesinde-
## 3 Data file: http://lambda.gsfc.nasa.gov/data/map/dr2/
pendently.Instead,whatisofinteresttoinvestigateisthechance
ancillary/wmap_kp2_r9_mask_3yr_v2.fits;
thataPDS-likecross-correlationsignaloccurs,giventhatS ξ is map projection: http://lambda.gsfc.nasa.gov/product/map/
aslowasthatwhichisobserved.Conservatively,wecancalcu- current/map_images/f02_int_mask_b.png
lateanupperlimittothisconditionalprobabilityifweusesim- 4 The maps can be downloaded from http://cosmo.torun.pl/
ulatedskymapswithS
ξ
valuesalittlehigherthantheobserved GPLdownload/MCMC/sims-from-LR08-project/.
estimateofS ξ .Moreover,hereweusethekp2galacticcutmask, 5 InverseNoiseCoadded3-year.

|     |     |     |     |     | B.F.Roukemaetal.:Poincarédodecahedralspaceparameters |     |     |     |     |     |     |     |     |     | 659 |

shouldnotaffect
Sincealotofthelarge-scalepowerinwhatareconsideredas spatialandprojectedangulardefinitionsofS ξ
thebestestimatesofthecosmologicalsignalintheWMAPdata thequestionsofinteresthere.
lieclosetotheGalacticPlane(e.g.Tegmarketal.2003),simu-
lationsbasedonsphericalharmonicswiththesameC’sasthis
|     |     |     |     |     |     |     | l   | 3. Method |     |     |     |     |     |     |     |

signalbutdifferentphaseswillmostofthetimehavehighlarge-
scale power which does not happen to lie inside the kp2 cut. The method of using Markov Chain Monte Carlo simulations
Hence,simulationsmadewiththeHinshawetal.(2007)C esti- to optimise the cross-correlationξ of temperaturefluctuations
|     |     |     |     |     |     |     | l   |     |     |     | C   |     |     |     |     |
| --- | --- 
matesandmaskedwiththekp2maskwill,ingeneral,haveS es- betweencopiesofthesurfaceoflastscattering(SLS)inthecov-
ξ
timateslargerthanthatwhichisactuallyobservedforthepartof eringspaceS3,modelledasS3 ⊂ R4,isdescribedinSect.3of
thesignaloutsideofthekp2cutratherthanapproximatelyequal
RBSG08.
toit. Since it is importantthat the choice of pairs of points is as
ThisisnotduetoanerrorintheHinshawetal.(2007)esti- uniformasthenatureoftheobservationsallows,theselectionof
mates(assumingasimplyconnectedmodel6).Eventhoughthese pointsonacopyoftheSLSinRBSG08 waschosenuniformly
estimatesforl≤30aremadeusingnearlythesamekp2cutthat on the SLS, i.e. on the 2-sphere. The binning into bins of pair
weusehere(Hinshawetal.2007,useakp2cutdegradedinres-
|     |     |     |     |     |     |     |     | separations | was calculated |     | only after | the | pair separations |     | have |

olution), the spherical harmonics are nevertheless functions of been calculated by applyinga holonomytransformationto one
the full sky. Hinshaw et al. (2007) use a maximum likelihood ofthemembersofthepair.
methodwhichusestheinformationfromthecutskytoinferthe Fromacomputationalpointofview,applyingtheholonomy
best estimate of the C values for these functions covering the is the mostintensive step in the calculation,requiringthe mul-
l
full sky. Unsurprisingly, it implicitly extrapolates from the cut 4×4 R4.
|     |     |     |     |     |     |     |     | tiplication | of a | matrix | by a 4-vector, |     | as a | rotation | in  |

skytothefullsky,andrecoverssomeoftheinformationmasked
Thismatrixcalculationiscarriedout12timesforagivenpairof
intheGalacticPlane. points,sinceallofthe12holonomytransformationsmappinga
Since we wish to test the chance that a PDS-like cross- pointtooneofitsneigbouringcopiesoftheSLSmustbeexam-
| correlation |     | signal | occurs | given | that S is | as low as | that which | ined. |     |     |     |     |     |     |     |

ξ
isobserved,wehavetwoobviousapproachestochoosefromin
|     |     |     |     |     |     |     |     | Theset | of20 holonomytransformationsthatmapsthe |     |     |     |     |     | fun- |

ordertohavesimulationswhicharestatisticallycomparablewith
|     |     |     |     |     |     |     |     | damental | domain | to the next | layer | in the | direction | of the | hy- |

theobservations.Oneapproachwouldbetoanalysethefullsky persphericalequatorcould, in principle,be used too. However,
for bothobservationsandsimulations. Inthis case, theS esti- for these to give matched circles as small as 5◦, this would re-
ξ
mates shouldbe approximatelyequal. However,a large partof quire the total matter-energy density to be Ω (cid:2) 1.03, which
tot
thesignalwouldbethatfrominsidetheGalacticPlane.Therisk
|     |            |         |                |     |                           |     |     | is uncomfortablyhigh |               | givenpresent |        | observationalestimates |           |     | of   |

| of  | implicitly | testing | the properties |     | of foregroundcontaminants |     |     | Ω                    |               |              |        |                        |           |     |      |
|     |            |         |                |     |                           |     |     | tot . To see         | this, replace | π/10         | in Eq. | (15)                   | of RBSG08 | by  | π/6, |
ratherthanofthecosmologicalsignalwouldbehigh. which is half the geodesic length of any member of this set
The other approach is to analyse the cut sky (with the kp2 of holonomy transformations (Clifford translations), and use
mask)forbothobservationsandsimulations.Thisdecreasesthe R = (c/H )(Ω −1)−1/2,whereR istheradiusofcurvature,
|     |     |     |     |     |     |     |     | C   | 0 tot |     |     | C   |     |     |     |

riskthatouranalysiswillbeaffectedbycontaminationfromthe i.e.theradiusofS3 modelledasa subsetofR4.Moreover,itis
GalacticPlane.However,forthecutsky,manyofthesimulations
|     |     |     |     |     |     |     |     | not clear | how a “generalised”twist |     |     | parameter | could | be  | used if |

will have S ξ higher than S ξ of the observations. In this case, bothsets(oryetfurthersets)ofholonomytransformationswere
it will be necessary to select those simulations with the lowest tobeusedinasingleestimateofthecross-correlationfunction.
valuesofS notgreaterthanS oftheobservationalmap. Thetwistforthissetofholonomytransformationsis±π/3,not
|     |     | ξ   |     | ξ   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- 
This will not give an exact statistical match between simu- ±π/5. For these reasons, we consider just the 12 immediately
| lations | and | observations. |     | However, | since | greater S | should in- |                                                      |     |     |     |     |     |     |     |

|         |     |               |     |          |       |           | ξ          | neighbouringcopiesofthefundamentaldomain,asinRBSG08. |     |     |     |     |     |     |     |
crease the chance of cross-correlations occurring, this should Inthispaper,wearguethatafteruniformlyselectingpoints
give an upper limit for estimating the probability of cross- on the 2-sphere, a filtering of these points is possible in a way
correlationsoccurringin a simply connectedmodel, i.e. a con- that excludes only those points that are certainly not members
servativeestimate.Thisistheapproachweadopthere. of any close SLS-SLS pairs, for a given maximum pair sepa-
|     | We estimate |     | S for each | of  | the observational |     | and simula- |                                                          |     |     |     |     |     |     |     |

|     |             |     | ξ          |     |                   |     |             | rationr 2 .Thisshouldenableshorteningthetimetofindagiven |     |     |     |     |     |     |     |
tionalusing
|     |     |     |     |     |     |     |     | numberofclosepairsforaconstantnumberofpointsN |     |     |     |     |     | ,aswell |     |

p
(cid:2) as finding a largernumber of close pairs for the same value of
|     | 2rSLS |     | r   |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----- 
≡ (r)]2 N , s in c e p oi n ts th at ar e c e r ta i n ly n o t m e m be r s o f a n y c lo s e p a ir
| S ξ |     | [ξ A | d   | ,   |     |     | (2) | p   |     |     |     |     |     |     |     |

r a r e r e je c te d b e fo re th e i te r a ti o n o v e r p a irs o f p o i n ts i s s ta r te d .
|     | rSLS |     | SLS |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---- 
Thelatterimprovementtothealgorithmshouldenablepractical
| wherer |     | istheradiusoftheSLS,ξ |     |     | (r)isthe(comoving)spa- |     |     |                                          |     |     |     |     |     |     |     |

|        | SLS |                       |     |     | A                      |     |     | useofthemethodforshorterpairseparations. |     |     |     |     |     |     |     |
tialauto-correlationfunctionasgiveninEq.(4)ofRBSG08,and
| r is | the comoving |     | spatial | separation | of  | a pair of points | on the |     |     |     |     |     |     |     |     |

SLS. This integral differs from that in Eq. (9) of Spergelet al. 3.1.Preselectionofpotentialmembersofclosepairs:α ,α
1 2
(2003),sinceherewefocusonspatialseparation,whileSpergel
Figures1and2showhowaclosepairusedinacross-correlation
etal.(2003)useanorthogonalprojectionoftheanglebetweena
|     |     |     |     |     |     |     |     | estimate | relates to | the two | copies of | the | SLS and | the angle | α±  |

pairofskypositions.Theminimumangularseparationusedby
thatseparatesit,onacopyoftheSLS,fromadodecahedralface
| the         | latter | is 60◦ ≈ | 1 rad, | so here     | we use | r forthe    | minimum |                                                          |     |     |     |     |     |     |     |

|             |        |          |        |             |        | SLS         |         | centre.Usingthesphericalcosineformula,thelowertrianglein |     |     |     |     |     |     |     |
| separation. |        | Provided | that   | we estimate | S      | in the same | way for |                                                          |     |     |     |     |     |     |     |
ξ
|     |     |     |     |     |     | thedifferencebetween |     | thetwofigureshastherelation |     |     |     |     |     |     |     |

bothobservationaldataandsimulations,
|     |     |     |     |     |     |     |     | x    | r   | π    | r   | π   |     |     |     |

|     |     |     |     |     |     |     |     | =cos | SLS | +sin | SLS |     |     |     |     |
## 6 Foramultiplyconnectedmodel,thedistributionsofthevariousa ’s cos cos sin cosα± (3)
|     |     |     |     |     |     |     | lm  | R   | R   | 5   | R   | 5   |     |     |     |
| --- | --- 
aretosomedegreedependentononeother,soamethodwhichassumes C C C
theyareindependentcanatbestgiveanapproximateresult. whereα+ andα− areforFigs.1and2respectively.

| 660 |     |     | B.F.Roukemaetal.:Poincarédodecahedralspaceparameters |     |     |        |     |           |     |         |            |     |             |

|     |     | r   |                                                      |     |     |        |     |           |     |         |            |     | ≤           |
|     |     |     |                                                      |     |     | Hence, | by  | symmetry, | for | a given | separation | r 2 | r SLS , the |

minimumandmaximumboundariesfordefininganannulus
≤α≤α+
|     | r   |     |     | r   |     | α−                                           |        |     |                  |     |         |          | (4)        |

|     | SLS |     |     | SLS |     |                                              |        |     |                  |     |         |          |            |
|     |     |     |     |     |     | on the SLS                                   | around | a   | dodecahedronface |     | centre, | in order | to in-     |
|     |     |     |     |     |     | cludeallpointsthatcanpotentiallybemembersofa |        |     |                  |     |         |          | close pair |
x
|     |     |     |     |     |     | separatedbyaspatialgeodesicdistanceofatmostr |     |     |     |     |     | 2   | forthecor- |

α
respondingpairofmatchedfacesofthefundamentaldomain,are
+
|     |     |     |     |     |     |         | ⎡             |       |           |        | ⎤       |     |     |

|     |     |     |     |     |     |         | ⎢⎢⎢⎢⎢⎣ cosrSL | ± r   | −         | r cosπ | ⎥⎥⎥⎥⎥⎦· |     |     |
|     |     |     |     |     |     |         |               | S     | 2 co s    | S L S  |         |     |     |
|     |     |     | π   | R   |     | α± =cos | −1            | R C   |           | R C    | 5       |     | (5) |
|     |     |     |     |     |     |         |               |       | r         | π      |         |     |     |
|     |     |     | 5   | C   |     |         |               | s i n | SL S s in |        |         |     |     |
|     |     |     |     |     |     |         |               |       | R C       | 5      |         |     |     |
Whenr 2 islargerthantheseparationofdodecahedralfacecen-
tres(Eq.(32)inRBSG08),i.e.when
|     |     |     |     |     |     |     | (cid:9) | (cid:10) |     |     |     |     |     |

r SLS π
|     |     |     |     |     |     | r >2R |     | −   | ,   |     |     |     | (6) |

|     | SLS |     | SLS |     |     | 2 C   | R   | 10  |     |     |     |     |     |
C
|                                           |     |     |     |                       |     | the derivation                      | leading |     | to the | expression | for                | α− in Eq. | (5) is no |

|                                           |     |     |     |                       |     | longervalid.Instead,thelowerlimitα− |         |     |        |            | shouldbesettozero. |           |           |
| Fig.1.Relationofaspatialgeodesicoflengthr |     |     |     | 2 joininga“close”pair |     |                                     |         |     |        |            |                    |           |           |
Asmentionedabove,thepreselectionenabledbyEq.(5)can
ofpointsinspacetotwocopiesoftheSLS,andtheangleα+separating
the member of the pair on theright-hand SLSfromthe dodecahedral beappliedintwoways:
facecentre,i.e.fromthespatialgeodesicjoiningthetwoSLScopies.
(i) apointthatfailstobeamemberofa“close”pairforagiven
Thisfigureshowsaspatialgeodesic“external”tothematchedcircles
|     |     |     |     |     |     | maximumseparationr |     |     |     | inallofthe12directionsofholon- |     |     |     |

(intersectionbetweenthetwocopiesoftheSLS).Thecentresofthetwo 2
copiesoftheSLS(2-spheres)areseparatedby(π/5)R C .SeeSect.3.1. omy transformations to adjacent copies of the point in the
|     |     |     |     |     |     | covering | space | can | be removed |     | from the | list of | uniformly |

selectedpoints;and
(ii) wheniteratingthroughpairsofpointsandholonomytrans-
|     |     |     |     |     |     | formations |     | g (i = | 1,...,12), | a   | pair of points | for | which at |

i
|     |     |     |     |     |     | least | one of | the two | points | does | not satisfy | the | condition |

≤
|     |     |     |     |     |     | α α+ | canberejectedwithoutcalculatingthespatialsepa- |     |     |     |     |     |     |

rationofthepair.
rL S r Whenr 2 islarge,α+willalsobelarge,andthesixpairsofannuli
|     | S   |     |     |     |     | maybesufficientlywidethattogethertheycoverthewholesky. |     |     |     |     |     |     |     |

2 r
|     |     |     | SLS |     |     | Inthiscase,effect(i)willnotoccur.Forasmallenoughsepara- |     |     |     |     |     |     |     |

|     | x   | α   |     |     |     |                                                         |     |     |     |     |     |     |     |
|     |     | −   |     |     |     | tionr ,theeffectshouldoccur.Inthatcase,morepointscanbe  |     |     |     |     |     |     |     |

uniformlyselectedfromS2accordingtoauniformdistribution,
|     |     |     | π   | R   |     |     |     |     |     |     |     |     |     |

andagaintested,untiltherequirednumberofpointsisobtained.
|     |     |     | 5   | C   |     |               |     |        |          |         |           |     |           |

|     |     |     |     |     |     | In that case, | a   | higher | fraction | (though | not 100%) | of  | pairs de- |
finedbythissetofpointswillbeusefulforthecross-correlation
|     |     |     |     |     |     | function        | calculation.  |                                        | This should       | increase | the   | number  | of pairs |

|     |     |     |     |     |     | per bin,        | especiallyfor |                                        | the smallestbins, |          | which | havethe | fewest   |
|     |     |     |     |     |     | numbersofpairs. |               | Thiswouldbeusefulforhighresolutioncal- |                   |          |       |         |          |
culations.Botheffects(i)and(ii)shouldincreasethecalculation
|     | SLS |     |     | SLS |     |                               |     |     |     |     |                       |     |     |

|     |     |     |     |     |     | speedforagivennumberofpointsN |     |     |     |     | ,sincetheyavoidhaving |     |     |
p
tocarryoutunnecessarymatrixmultiplications.
| Fig.2.AsforFig.1,showingaspatialgeodesic,oflengthr |     |     |     |     | ,“internal” |     |     |     |     |     |     |     |     |

tothematchedcircles,andangleα−separatingthememberofthepair
3.2.Useofpreselectiononthefive-yearWMAPdata
ontheright-handSLSfromthedodecahedralfacecentre.
TheMCMCanalysisisperformedasinRBSG08,usingtheILC
|     |     |     |     |     |     | and TOH | five-year | WMAP |     | data (Sect. | 2.1), | but including | the |

smallestseparationbin,i.e.usingthefullrangeofseparations
| Clearly,α+ | ismaximisedwhen |     | xismaximised.Forfixedr |     |     |     |     |     |     |     |     |     |     |

andr ,xismaximisedwhenx=r +r ,i.e.whentheupper d/r <40/90, (7)
| SLS |     |     | SLS | 2   |     | SLS |     |     |     |     |     |     |     |

triangledegeneratesintoasinglelinesegment.Hence,theangle
| ismaximisedwhenx=r |                 | +r            |      |                  |          | i.e.             |     |     |     |     |     |     |     |

| α+                 |                 | SLS           | 2 .  |                  |          |                  |     |     |     |     |     |     |     |
| Similarly,         | α− is minimised | when          | x is | minimised,       | provided | (cid:3)4.4h−1Gpc |     |     |     |     |     |     |     |
|                    |                 |               |      |                  |          | d                |     |     |     |     |     |     | (8) |
| that r             | ≤ r , which is  | the situation |      | most interesting | for      |                  |     |     |     |     |     |     |     |
| 2                  | SLS             |               |      |                  |          |                  |     |     |     |     |     |     |     |
the SLS-SLS cross-correlation method, since close pairs are for Ω = 1.01, matter density Ω = 0.28 and SLS redshift
|     |     |     |     |     |     | tot |     |     |     | m   |     |     |     |

=1100,correspondingapproximatelytoanglesontheSLS
| the most | useful. For fixed | r 2 and | r SLS , | x is minimised | when | z SLS   |              |     |     |     |     |     |     |

| =        | −                 |         |         |                |      | (cid:3) | (cid:3) 25◦. |     |     |     |     |     |     |
x r r , i.e. when the upper triangle degenerates into 0 θ d All other parameters are kept as in Sect. 3.6
| SLS | 2   |     |     |     |     |     |     |     |     |     |     |     |     |

a single line segment. Hence, the angle α− is minimised when of RBSG08. In particular, this includes the five parameters for
x=r −r . orientationofthefundamentaldodecahedron(galacticlongitude
| SLS | 2   |     |     |     |     |     |     |     |     |     |     |     |     |


|     |     |     |     |     | B.F.Roukemaetal.:Poincarédodecahedralspaceparameters |     |     |     |     |     |     |     |     |     | 661 |

and latitude of oneface centre (l,b)and a rotationparameterθ Table1.Exampleofbenchmarkingona3GHzprocessora.
aroundtheaxisdefinedby(l,b)),thematchedcirclesizeαand
| the “generalised”twist |      |               | phase | φ when   | matchingopposite |     | faces.   |     |           |     |     |     |     |     |     |

|                        |      |               |       |          |                  |     | circles7 | α   | r         | α   | b N | t   | c   | N d | N d |
| The GPL                | (GNU | GeneralPublic |       | Licence) | program          |     |          | is  | 2         |     | +   | p   |     | A   | C   |
|                        |      |               |       |          |                  |     |          | ◦   | ≈h− 1 Gpc |     | ◦   |     | s   |     |     |
used.
|     |     |     |     |     |     |     |     | 5   | 0.4 | ... | 1000 | 5   |       | 1317 | 52   |

|     |     |     |     |     |     |     |     | 5   | 0.4 | ... | 2000 | 22  |       | 5268 | 206  |
|     |     |     |     |     |     |     |     | 5   | 0.4 | ... | 8000 | 375 | 83476 |      | 3900 |
3.3.Analysisofsimulations
|     |     |     |     |     |     |     |     | 5   | 4.4 | ... | 1000 | 5   |     | 1317 | 52  |

AlthoughthemethodpresentedinSect.3.1shouldspeedupthe 5 4.4 ... 2000 23 5268 206
|     |     |     |     |     |     |     |     | 5   | 4.4 | ... | 8000 | 377 | 83476 |     | 3900 |

calculation,analysingalargenumberofsimulationsisstilltime-
|            |       |     |          |     |                    |     |         | 5   | 0.4 | 13.6 | 1000 | 0   |       | 6994 | 1911 |

| consuming. | Here, | we  | estimate | S   | for 50 simulations |     | and the |     |     |      |      |     |       |      |      |
|            |       |     |          | ξ   |                    |     |         | 5   | 0.4 | 13.6 | 2000 | 2   | 28085 |      | 7860 |
WMAPobservationalmapdescribedinSect.2.2andselectthose
|                  |     |                                       |             |     |               |          |      | 5   | 0.4 | 13.6 | 8000 | 41  | 449308 |      | 126395 |

| 20 simulations   |     | whose                                 | S estimates |     | are smallest, | provided | that |     |     |      |      |     |        |      |        |
|                  |     |                                       | ξ           |     |               |          |      | 5   | 4.4 | 45.0 | 1000 | 0   |        | 1317 | 52     |
| S isnotlessthanS |     | oftheobservationalmap.Ineachestimate, |             |     |               |          |      |     |     |      |      |     |        |      |        |
| ξ                |     | ξ                                     |             |     |               |          |      | 5   | 4.4 | 45.0 | 2000 | 3   |        | 5268 | 204    |
10000pointsselectedrandomlyfromauniformdistributionon 5 4.4 45.0 8000 53 83476 3880
theskyoutsideofthekp2maskwereused.Usingeachofthese 60 0.4 ... 1000 5 1408 192
20 simulations and the observationalmap, four MCMC chains 60 0.4 ... 2000 23 5650 736
withrandomstartingpointsintheparameterspacedescribedin 60 0.4 ... 8000 354 90242 12070
| Eq.(28)ofRBSG08arecarriedout. |     |     |     |     |     |     |     | 60  | 4.4 | ...  | 1000 | 5   |        | 1408 | 192   |

|                               |     |     |     |     |     |     |     | 60  | 4.4 | ...  | 2000 | 24  |        | 5650 | 736   |
|                               |     |     |     |     |     |     |     | 60  | 4.4 | ...  | 8000 | 369 | 90242  |      | 12070 |
| 4. Results                    |     |     |     |     |     |     |     | 60  | 0.4 | 62.9 | 1000 | 0   |        | 3532 | 1518  |
|                               |     |     |     |     |     |     |     | 60  | 0.4 | 62.9 | 2000 | 3   | 14290  |      | 5986  |
| 4.1.Benchmarking              |     |     |     |     |     |     |     | 60  | 0.4 | 62.9 | 8000 | 48  | 228426 |      | 94887 |
|                               |     |     |     |     |     |     |     | 60  | 4.4 | 90.9 | 1000 | 2   |        | 1408 | 183   |
Anexamplesetofcalculationtimesandnumberofpairsinthe
|          |            |     |     |          |       |        |              | 60  | 4.4 | 90.9 | 2000 | 8   |       | 5650 | 706   |

| smallest | separation | bin | are | shown in | Table | 1, for | one calcula- |     |     |      |      |     |       |      |       |
|          |            |     |     |          |       |        |              | 60  | 4.4 | 90.9 | 8000 | 130 | 90242 |      | 11536 |
tionoftheauto-correlationandcross-correlationfunctionsatan
= 5◦ = 60◦, a The pseudo-random number generator has the same initial seed for
| arbitrary | PDS | orientation | and | twist, | for α | and | α   |     |     |     |     |     |     |     |     |

eachcalculation;banestimateofα+fromEq.(5)isshowninthecases
| which determine |     | the ratio | r   | /R . | The speed-upfactorsrange |     |     |     |     |     |     |     |     |     |     |

SLS C wherepairpreselectionasdescribedinSect.3.1isused;c calculation
| fromabout3–10,dependingonbothαandr |     |     |     |     |     | .   |     |                                        |     |     |     |     |     |      |            |

|                                    |     |     |     |     | 2   |     |     | time;d numbersofpairsinthesmallestbinN |     |     |     |     | , N | forξ | ,ξ respec- |
For d < r = 4.4 h−1Gpc, the “annulus outer radii” are A C A C
|     | 2   |     |     |     |     |     |     | tively. |     |     |     |     |     |     |     |

=45.0◦,90.9◦forα=5◦,60◦respectively.Thisisclearlytoo
α+
largetoallowanyremovalofpointsfromthelistofpotentially
useful pairs, i.e. effect (i) in Sect. 3.1 does not occur: N and In a full MCMC chain, the matched circle size α will vary
A
| N are | negligiblyaffected |     | by  | the pair | preselection |     | mechanism. |     |     |     |     |     |     |     |     |

C between the limits illustrated in Table 1. The actual speed-up
However,thelabellingofpointstorecordwhichannulitheycan
|     |     |     |     |     |     |     |     | factor (and | increase | in  | numbers | of pairs | per | bin if | this occurs) |

potentiallybepairsofdoesyieldaspeed-upthrougheffect(ii),
willdependontheparticularpathoftheMCMCchainthrough
| i.e.byfactorsofabout7and3forα=5◦ |     |     |     |     | and60◦respectively. |     |     |           |        |        |              |         |     |        |             |

|                                  |     |     |     |     |                     |     |     | parameter | space. | In the | calculations | leading |     | to the | results de- |
Foramuchsmallermaximumpairseparation,i.e.d < r = scribedbelow,therange5◦ <α<60◦wasretained.

| 0.4 h−1Gpc,  | even                                        | though | the | annulusouter |     | radii are | still quite |     |     |     |     |     |     |     |     |

| large,i.e.α+ | =13.6◦,62.9◦forα=5◦,60◦respectively,bothef- |        |     |              |     |           |             |     |     |     |     |     |     |     |     |
4.2.Parameterestimatesfromthefive-yearWMAPdata
fects(i)and(ii)occur.Thatis,notonlyisthereaspeed-upbya
factorofabout7–10,butthereisalsoanincreaseinthenumber
|     |     |     |     |     |     |     |     | For both | maps | of the five-year |     | data | as described |     | in Sect. 2.1 |

of pairsin thesmallest binforcalculatingthe cross-correlation =
|                                                     |     |     |     |     |     |     |     | (ILC and     | TOH),   | N        | 16                  | MCMC | chains | were         | run, each |

| function,byfactorsofabout30and7forα=5◦and60◦respec- |     |     |     |     |     |     |     |              |         | c h ai n |                     |      |        |              |           |
|                                                     |     |     |     |     |     |     |     | startingwith | differe | n t r    | andomseeds,usingthe |      |        | kp2mask.Each |           |
tively.
|              |     |        |         |         |      |            |     | run had                                  | 12000 | steps and | the first | 2000steps |     | of each | were dis- |

| In practice, |     | use of | a small | maximum | pair | separation | bin | to                                       |       |           |           |           |     |         |           |
|              |     |        |         |         |      |            |     | carded8.Figure3showstheskypositions(l,b) |       |           |           |           |     |         | impliedby |
i=1,12
getcosmologicallysignificantresultswillbecomplicatedbythe
relativelylargercontributionsfromtheDopplerandISWeffects, the (l,b,θ) triples in the MCMC chains for which P > 0.5
(Eq.(25),RBSG08),fortheILCandTOHversionsofthefive-
| from residual | foreground |     | contamination, |     | from | the | differences |           |               |     |       |     |               |     |            |

|               |            |     |                |     |      |     |             | year WMAP | observational |     | data. | The | “probability” |     | function P |
betweenvariousversionsoftheall-skyCMBmapatthesereso-
usedforoptimisationbytheMCMCprocedureisthatdefinedin
| lutions | (Aurich | et al. | 2006), | and from | the absence |     | of the large |     |     |     |     |     |     |     |     |

Eq.(25)inRBSG08.Thisisnotatrueprobabilityfunction.
| scale signal. | Nevertheless, |                | the | concern | expressed      |     | in Sect. 5.5 |           |          |           |         |            |     |              |            |

|               |               |                |     |         |                |     |              | Similarly | to       | what was  | done    | in RBSG08, |     | the 16       | chains are |
| of RSBG08     | that          | improvementsto |     | the     | algorithmwould |     | be geo-      |           |          |           |         |            |     |              |            |
|               |               |                |     |         |                |     |              | grouped   | together | into four | groups, | each       | of  | four chains. | For a      |
metricallyquitecomplex,attheriskofintroducingbiasestothe
|     |     |     |     |     |     |     |     | givengroup,steps2001to |     |     | 12000fromeachofthefourchains |     |     |     |     |

method,appearstohavebeenovercome,reducingoneobstacle
areconcatenated.
tosmallscaleworkusingthistypeofmethod.
|     |     |     |     |     |     |     |     | We make | the | convergencerequirements |     |     |     | a little | more strin- |

## 7 Version circles -0.3.2.1wasusedforcalculatingtheMCMCchains gent than was described in Sect. 4.1 of RBSG08. That is, we
= 30◦
for the five-year WMAP maps, and version circles -0.3.8 was used start from an initial angularradiusof β (coveringmost

forcalculatingthechainsfortheINC3observational andsimulational ofthesphere),decreaseby1◦forthenext20iterations,andthen
| maps. Various | versions |     | of circles | are | downloadable | from | http:// |     |     |     |     |     |     |     |     |

adjani.astro.umk.pl/GPLdownload/dodec/. These and earlier 8 The MCMC chains used in this paper can be downloaded for in-
versionsofthesoftwarerequiremediumtoadvanced gnu/linux , for- dependent analysis from the file http://adjani.astro.umk.pl /
tran 77andCexperienceforascientificuser. GPLdownload/MCMC/mcmc_RBG08.tbz

| 662 |     |     |     | B.F.Roukemaetal.:Poincarédodecahedralspaceparameters |     |     |     |     |     |     |     |     |     |     |     |     |

Table2.Skypositionsofthebestestimateofthesixdodecahedralface
centresforthefive-yearILCmapwiththekp2mask.
|     |     |     |     |     |     |     |     |     | P   | ia  | n   |     | l b | σ(cid:10)(l,b)(cid:11) |     |     |

min
|     |     |     |     |     |     |     |     |     |      |     |      |       | ◦ ◦  |     | ◦   |     |

|     |     |     |     |     |     |     |     |     | 0.4  | 7   | 5141 | 182.8 | 62.3 | 1.1 |     |     |
|     |     |     |     |     |     |     |     |     | 0.4  | 12  | 5239 | 305.5 | 44.4 | 1.2 |     |     |
|     |     |     |     |     |     |     |     |     | 0.4  | 3   | 7097 | 45.0  | 49.5 | 0.7 |     |     |
|     |     |     |     |     |     |     |     |     | 0.4  | 5   | 5812 | 115.9 | 19.5 | 1.2 |     |     |
|     |     |     |     |     |     |     |     |     | 0.4  | 8   | 5056 | 174.6 | –3.0 | 2.9 |     |     |
|     |     |     |     |     |     |     |     |     | 0.4  | 10  | 4707 | 239.8 | 13.9 | 2.1 |     |     |
|     |     |     |     |     |     |     |     |     | 0.5b | 7   | 2736 | 181.1 | 62.2 | 1.4 |     |     |
|     |     |     |     |     |     |     |     |     | 0.5  | 12  | 2838 | 305.7 | 44.5 | 1.3 |     |     |
|     |     |     |     |     |     |     |     |     | 0.5  | 3   | 3712 | 45.4  | 49.3 | 0.7 |     |     |
|     |     |     |     |     |     |     |     |     | 0.5  | 5   | 3005 | 114.6 | 18.7 | 1.6 |     |     |
|     |     |     |     |     |     |     |     |     | 0.5  | 8   | 2732 | 178.1 | –0.5 | 1.6 |     |     |
|     |     |     |     |     |     |     |     |     | 0.5  | 10  | 2570 | 239.9 | 13.8 | 1.6 |     |     |
|     |     |     |     |     |     |     |     |     | 0.6  | 7   | 1429 | 179.3 | 62.6 | 1.1 |     |     |
|     |     |     |     |     |     |     |     |     | 0.6  | 12  | 1487 | 306.0 | 44.3 | 1.2 |     |     |
|     |     |     |     |     |     |     |     |     | 0.6  | 3   | 1919 | 45.5  | 48.8 | 0.8 |     |     |
|     |     |     |     |     |     |     |     |     | 0.6  | 5   | 1544 | 113.6 | 18.4 | 2.0 |     |     |
|     |     |     |     |     |     |     |     |     | 0.6  | 8   | 1387 | 175.6 | –1.6 | 3.0 |     |     |
|     |     |     |     |     |     |     |     |     | 0.6  | 10  | 1419 | 237.7 | 14.5 | 1.6 |     |     |
a
ThefacecentresareorderedaccordingtotheorderinginTable1of
RBSG08.Theother6facesaredirectlyoppositewithidenticalerrors;
|     |     |     |     |     |     |     |     | b            |     | P       | = 0.5 |             |        |        |       |        |

|     |     |     |     |     |     |     |     | the estimate |     | for min |       | corresponds | to the | points | shown | in the |
upperpanelofFig.3,basedon160000stepsofMCMCchains.
|     |     |     |     |     |     |     |     | multi-dimensional |     | parameter |     | space, | whereas | the | latter | is the |

peakofaprojecteddistributionusingasingleparameter.
|     |     |     |     |     |     |     |     | As  | was discussed |     | in Sect. | 4.2 | of RBSG08, | when | α   | is not |

Fig.3.Fullskymap[Lambertazimuthalequalareaprojection(Lambert too large, small changes in the comoving separation between
1772),centredontheNorthGalacticPole(NGP),withthe0◦meridian pairs lead to relatively large changesin α. Does the use of the
asthepositiveverticalaxisandgalacticlongitudeincreasingclockwise] smallestbininthepresentanalysis,and/ortheuseoftheslightly
showingtheoptimalorientationofdodecahedralfacecentresbasedon improved quality between the three-year and five-year WMAP
160000stepsin16MCMCchains,usingthefive-yearILCmap(upper
datahelpovercomethelargeuncertaintyinα?Visualinspection
| panel) and | the five-year |     | TOH map | (lower | panel), | and the kp2 | mask, |         |            |      |          |     |           |         |           |     |

|            |               |     |         |        |         |             |       | of Fig. | 4 suggests | that | the MCMC |     | chains on | the ILC | five-year |     |
showingfacecentresforwhichP>0.5. mapfavour22◦ 35◦,whilethoseontheTOHmapfavour
(cid:3)α(cid:3)
|                  |     |      |       |            |               |     |           | 15◦ (cid:3)    | α (cid:3) 35◦.      | The | problemof | approximatedegeneracyin |     |     |            | α,  |

|                  |     |      |       |            |               |     |           | which is       | presumablysensitive |     |           | to moderatelevelsof     |     |     | systematic |     |
| remain constant  |     | at β | = 10◦ | until      | the iteration | for | that face |                |                     |     |           |                         |     |     |            |     |
|                  |     | j≥21 |       |            |               |     |           | error,remains. |                     |     |           |                         |     |     |            |     |
| number converges |     | or   | until | a total of | 40 iterations | has | been      |                |                     |     |           |                         |     |     |            |     |
reached.Theanalysesofthefourconcatenatedgroupsofchains
4.3.Simulations
givewhatareconsideredtobefourindependentestimatesinor-
der to get an estimate of the uncertainties due to our MCMC EstimatesofS
|     |     |     |     |     |     |     |     | 4.3.1. |     |     | ξ   |     |     |     |     |     |

estimationmethod.
|                                         |     |     |     |     |     |              |     | ThevalueofS |     | (Eq.(2))intheINC3observationalmap(using |     |     |     |     |     |     |

| Theresultingnumericalestimatesarelisted |     |     |     |     |     | inTable2.The |     |             |     | ξ                                       |     |     |     |     |     |     |
thekp2mask)is
| columnsshowminimum“probability”P |     |     |     |     | min ,facenumberi,num- |     |     |     |     |     |     |     |     |     |     |     |

bernofMCMCstepscontributingtotheestimateobtainedfrom
|           |            |          |           |     |                |     |         | SINC3 =963(μK)4. |     |     |     |     |     |     |     | (9) |

| the final | iteration, | galactic | longitude |     | l and latitude | b,  | and the | ξ                |     |     |     |     |     |     |     |     |
standarderrorinthemeanbetweenthefourestimatesofdiffer-
|     |     |     |     |     |     |     |     | The 50 | simulations |     | have S | in the | range 1170(μK)4 |     | <   | S < |

entsetsofMCMCchains,ingreatcircledegrees,σ(cid:10)(l,b)(cid:11).These ξ ξ
8645(μK)4,
|           | differ |               |     |           |     |        |       |         | i.e.              | up to | about | an order  | of magnitude |      | higher | S ξ    |

| values do | not    | significantly |     | fromthose | in  | Tables | 1 and | 4       |                   |       |       |           |              |      |        |        |
|           |        |               |     |           |     |        |       | than in | the observations. |       | As    | mentioned | in Sect.     | 2.2, | this   | is be- |
(forthekp2mask)ofRBSG08.
|             |        |           |        |            |           |              |         | cause the                                                | WMAP        | cosmologicalsignal |        |         | hasa           | lotof | powerclose |        |

| The MCMC    |        | states    | for α  | and φ in   | the final | radii of     | conver- |                                                          |             |                    |        |         |                |       |            |        |
|             |        |           |        |            |           |              |         | to the Galactic                                          |             | Plane              | and we | use     | the kp2 cut    | sky.  | In order   | to     |
| gence, and  | their  | means     | and    | standard   | errors    | in the mean, | are     |                                                          |             |                    |        |         |                |       |            |        |
|             |        |           |        |            |           |              |         | use the                                                  | simulations | best               | able   | to test | the hypothesis |       | that       | a sim- |
| shown in    | Fig. 4 | and Table | 3.     | Histograms | of the    | distribution | of      |                                                          |             |                    |        |         |                |       |            |        |
|             |        |           |        |            |           | differ       |         | plyconnecteduniversewithanobservationallyvalidlargescale |             |                    |        |         |                |       |            |        |
| φ are shown | in     | Fig. 5.   | Again, | these      | values do | not          | sig-    |                                                          |             |                    |        |         |                |       |            |        |
auto-correlationcangiveaPDS-likesignal,weselectthe20of
| nificantly | from | those | in Table | 2 of | RBSG08. | The TOH | map |                     |     |     |                       |     |     |     |     |     |

|            |      |       |          |      |         |         |     | thesewiththelowestS |     |     | values,i.e.intherange |     |     |     |     |     |
shows a small offset between the best estimate of φ found(for ξ
P > 0.5)usingourconvergencealgorithmandthatatwhichthe
|              |     |                 |     |           |     |        |             | 1170(μK)4 | <S  | <3782(μK)4, |     |     |     |     |     | (10) |

|              |     |                 |     |           | =   | 30.4◦, |             |           |     | ξ           |     |     |     |     |     |      |
| histogramofφ |     | statespeaks.The |     | formerisφ |     |        | i.e. a lit- |           |     |             |     |     |     |     |     |      |
36◦,
tle below while the latter (lower panel of Fig. 5) is a few i.e.withuptoabout3.9timeslargerS ξ thanintheobservations.
degreesabove36◦.
The differencecan reasonablybe attributed Since atlargescales (outsideofthe kp2cut),these simulations
to the fact that the former uses a convergence algorithm in are morecorrelatedthan the observations,we shouldobtain an

|     |     |     | B.F.Roukemaetal.:Poincarédodecahedralspaceparameters |     |     |     |     |     |     |     |     |     |     | 663 |

Table3.Estimatesofmatchedcircleradiusαandtwistphaseφfromthe
IntegratedLinearCombination(ILC)andTegmarketal.(2003)(TOH)
versionsofthefive-yearWMAPdata.

|     |     |     |     |     |     |     | Map | P   | na  |     | α σ(cid:10)α(cid:11) |     | φ σ(cid:10)φ(cid:11) |     |

min
|     |       |     |     |     |     |     |     |     |         |      | ◦   | ◦      | ◦   | ◦   |

|     |       |     |     |     |     |     | ILC | 0.4 | 5508.67 | 20.3 | 0.7 | 38.7   | 1.6 |     |
|     |       |     |     |     |     |     | ILC | 0.5 | 2932.17 | 20.5 |     | 1 37.8 | 1.2 |     |
|     | 0 0 0 |     |     |     |     |     | ILC | 0.6 | 1530.83 | 20.1 | 0.7 | 39.8   | 1.1 |     |
φ φ φ
|     |     |     |     |     |     |     | TOH | 0.4 | 4802.08 | 21.2 | 1.4 | 30.6 | 4.8 |     |

|     |     |     |     |     |     |     | TOH | 0.5 | 2955.58 | 20.4 | 0.8 | 32.1 | 2.6 |     |
|     |     |     |     |     |     |     | TOH | 0.6 | 1655.92 | 20.3 | 0.7 | 27.5 | 5.5 |     |
a
−100 −100 −100 Thenumberofstepsncanbeanon-integersinceforagivenMCMC
step,itispossiblethatsomeofthefacecentresfallwithintheconver-
|     |     |     |     |     |     | gence | radius | of the | final iteration | as  | described | in Sect. | 4.2, | but other |

facecentresdonot.
|     | 0 0 0 10 10 10 | 20 20 20 | 30 30 30 | 40 40 40 | 50 50 50 60 60 60 |     |     | 888000000 |     |     |     |     |     |     |

α α α
666000000

NNN 444000000
| φ φ φ | 0 0 0 |     |     |     |     |     |     | 222000000 |     |     |     |     |     |     |

|     |                |     |     |     |     |     |     |     | −−−111000000 |     | 000 | 111000000 |     |     |

|     | −100 −100 −100 |     |     |     |     |     |     |     |              |     | φφφ |           |     |     |
888000000
666000000
|     | 0 0 0 10 10 10 | 20 20 20 | 30 30 30 | 40 40 40 | 50 50 50 60 60 60 |     |     |     |     |     |     |     |     |     |

α α α
Fig.4. Distribution of α and φ states where P > 0.5 in the MCMC NNN 444000000
chainsofthedodecahedralsolutionusedinTable2,fortheILC(upper
| panel) andTOH(lowerpanel) |     |     | maps.Inthisandsimilarfigures,lines |     |     |     |     |     |     |     |     |     |     |     |

indicating±36◦areshown.Thesearenotfittothedata.
222000000
| upper limit | to the the | frequency | of detecting | PDS-like | signals, |     |     |     |     |     |     |     |     |     |

assumingthatthePDShypothesisiswrong.

Asacheckontheamountoflargescalepowerpresentinthe −−−111000000 000 111000000
| GalacticPlaneindifferentversionsofthemapofcosmological |     |     |     |     |     |     |     |     |     |     | φφφ |     |     |     |
| ------------------------------------------------------ 
√
signal,weestimateS fortheILCandTOHfive-yearmapswith Fig.5.HistogramofthetwistangleφshowninFig.4,with N error
ξ
andwithoutthekp2mask.Table4showstheseestimates.Both bars,fortheILC(upperpanel)andTOH(lowerpanel),excludingstates
| mapshavemuchmorepowerwithoutthecutthanwiththecut, |           |       |                |     |                | withα≤15◦. |     |     |     |     |     |     |     |     |

| as expected.                                      | Moreover, | while | the difference | in  | estimates of S |            |     |     |     |     |     |     |     |     |
ξ
differs
| for the | two maps | by  | nearly a | factor of | two for the full |     |     |     |     |     |     |     |     |     |

differs
sky, it by only 10% for the cut sky. This confirms the remains computationally prohibitive. For this reason, we carry
advantageinanalysingthecutskyratherthanthefullsky:there outonlyasmallnumberofMCMCchains(four)oneachdataset
is approximateconsensusbetween these two differentmethods (INC3observationaldatasetorsimulation),anddonotattempt
| ofgeneratingthemap.TheINC3estimateofS |     |     |     |     | = 963(μK)4is |     |     |     |     |     |     |     |     |     |

ξ to estimate uncertainties on the individual optimal parameters
| alsoclosetothesetwoestimates. |     |     |     |     |     | foragivendataset. |          |             |          |             |            |        |       |         |

|                               |     |     |     |     |     |                   | We first | concatenate | together |             | steps 2001 | to     | 12000 | of each |
|                               |     |     |     |     |     | chain             | in a     | group,      | i.e. we  | ignore 2000 | burn-in    | steps. | This  | con-    |
4.3.2. MCMCchains
|     |     |     |     |     |     | catenated |     | chain is | considered | to be | a single | chain | for | the iter- |

Whilethespeedimprovementintroducedinthispapermakesit ative procedureof estimatingparametervalues. We modifythe
possibletoanalyseasetofsimulationsratherthanjustanobser- methodofchoosinganinitialroughestimateoftheoptimaldo-
vationalmap,carryingoutlargenumbersofMCMCchainsstill decahedralfacecentrepositionsthatisusedtostarttheiterations

| 664      |                                               | B.F.Roukemaetal.:Poincarédodecahedralspaceparameters |     |     |     |     |     |

| Table4.S | estimateswithandwithoutthekp2maskfortheILCand |                                                      |     |     |     |     |     |
ξ
TOHfive-yearmaps.
|                                                 | Map             | kp2 Nomask  |                          |          |     |     |     |

|                                                 |                 | (μK)4 (μK)4 |                          |          |     |     |     |
|                                                 | ILC             | 1012 4851   |                          |          |     |     |     |
|                                                 | TOH             | 1136 2749   |                          |          |     |     |     |
| Fig.6. Full                                     | sky map showing | the optimal | orientation of dodecahe- |          |     |     |     |
| dral facecentresbasedon40000stepsin4MCMCchains, |                 |             |                          | usingthe |     |     |     |
three-yearINCmapandthekp2mask,showingfacecentresforwhich
P>0.5.
| towardsa | morepreciseestimatebyrandomlyselectinga |     |     | setof |     |     |     |

dodecahedralfacecentres[(l,b)chosenfromauniformdistribu-
|             |               |                       |               | Fig.7. Full       | sky map showing | the optimal orientation | of dodecahedral     |

| tion on S2, | θ chosen from | a uniformdistribution | on (0,2π/5).] |                   |                 |                         |                     |
|             |               |                       |               | face centresbased | on40000         | stepsin4MCMC            | chains, usingthetwo |
Thisriskscausingtheconvergencetobelessaccurate,butsince simulatedthree-year INCmapswithlowest S estimates(simulations
ξ
this isappliedinthe same wayforbothsimulationsandobser- 92 and 90, in the upper and lower panels respectively), and the kp2
vations,thisshouldnotintroduceanystatisticalbiasforcompar- mask,showingfacecentresforwhichP>0.5.
isonofobservationstosimulations.
| We also | make our | iteration a little more | stringent than | that |     |     |     |

describedinSect.4.2.Inthefirstiterationofparameterestima- of the observations), are shown in Fig. 7. In one case, there is
tion, we estimate the dodecahedralface centresstarting from a clearlyaprobleminconvergingonasinglesetofdodecahedral
random initial set as just described, and in the following itera- facecentres,whileintheother,theredoesappeartobemoreor
tions,weconvergeonbothdodecahedralfacescentresandα,φ lessconvergencetoasinglesolution.
| simultaneously.Thevaluesofβ |     | (seeSect.4.2)areunchanged. |     |     |     |     |     |

j
= 10◦
| Thesetofpointswithintheconvergenceradiusβ |     |     | j≥21 | is                               |     |     |     |

|                                           |     |     |      | 4.3.4. Circlesizeαandtwistphaseφ |     |     |     |
usedforthefinalestimatesofαandφ.
Figure8showsthatconvergenceinαandφoccursfortheINC3
4.3.3. Optimaldodecahedronorientation:(l,b,θ)space observationalmapinasimilarwaytothatofthefive-yearobser-
vationalmaps.Incontrast,Fig.9showsthatthetwosimulations
Figure 6 shows the optimal set of face centres resulting from whoseS estimatesbestmatchthatofthedata,i.e.thosewhose
ξ
thefourMCMCchainsfortheINC3observationalmap.While best dodecahedral face centres are shown in Fig. 7, both “es-
the sharpnessof the optimalsignaldoesnotappearas strongly cape” towards the lower limit α = 5◦. The median circle size
|     |     |     |     | = 5◦ |     | effectcan |     |

asintheresultsusinglargernumbersofchainsinRBSG08and is α in both cases. This be expecteddue to the
in Fig. 3 for the five-year data here, it is clearly consistent in increasedrelativePoissonerrorwhencomparingfewernumbers
position.Sinceweusemanyfewerchainshere,itisunsurprising ofpairsofpixels.Aurich(2008)foundasimilareffect,describ-
that the signal appears weaker. This should not be a problem ingitas“drifting”towards“largeL”,whichcorrespondshereto
form the present purpose, since the uncertainties from using a smallα.Severalpreviousauthorshavefoundthatindependently
smallnumberofchainsshouldbestatisticallyequivalentforboth
ofwhetherornotacosmictopologysignalispresent,relatively
INC3observationaldataandsimulations. highercross-correlationsforzeroseparationpairs,i.e.forpairs
Ontheotherhand,therelativeweaknessofthesignalandthe onexactlymatchedcircles,havebeenfoundtooccurasthecircle
smallernumbersofchainsrequireusingslightlylowerminimum sizeαapproacheszero.Forexample,seeFig.2inCornishetal.
probability thresholds for estimating the best solution. Below, (2004),Figs.4–6inRoukemaetal.(2004),orFig.3inLew&
| we cite results | for P | = 0.3,0.4,0.5 | rather than the | earlier                                                |     |     |     |

|                 | min   |               |                 | Roukema(2008),wherevariousdefinitionsofanormalisedcor- |     |     |     |
=0.4,0.5,0.6.
thresholdsofP min relationstatisticS areshowntoincreaseasαdecreasestowards
Examplesofoptimaldodecahedralorientations,forthetwo zero.Hence,itcanbeexpectedthatMCMCchainswillbedrawn
simulationswhoseS estimatesarelowest(i.e.areclosesttothat towardsthelowerαlimit.
ξ

|                |             |     | B.F.Roukemaetal.:Poincarédodecahedralspaceparameters |     |     |                |     |     | 665 |

|                | 100 100 100 |     |                                                      |     |     | 100 100 100    |     |     |     |
|                | 0 0 0       |     |                                                      |     |     | 0 0 0          |     |     |     |
| φ φ φ          |             |     |                                                      |     |     | φ φ φ          |     |     |     |
| −100 −100 −100 |             |     |                                                      |     |     | −100 −100 −100 |     |     |     |
0 0 0 10 10 10 20 20 20 30 30 30 40 40 40 50 50 50 60 60 60 0 0 0 10 10 10 20 20 20 30 30 30 40 40 40 50 50 50 60 60 60
|                     |          |          | α α α   |              |      |     |     | α α α |     |

| Fig.8. Distribution | of α and | φ states | where P | > 0.5 in the | MCMC |     |     |       |     |
chainsfortheINC3observationalmap.

| In cases | where this | occurs, chains | spend | a large amountof |     |     |     |     |     |

timeatthislimit,butcannotgobelowit.Forthisreason,theme-
dianoftheαestimates(aboveaminimum“probability”usedin
| theMCMCchains,e.g.P> |     | P =0.5),shouldmoreaccurately |     |     |     | φ φ φ 0 0 0 |     |     |     |

min
representtheoptimalregionfavouredbytheMCMCchainsthan
themean.Thus,hereweusethemedianofα.
Figure10showsthatnearlyallthesimulationsescapetothe
lowerαlimit.Mostofthesimulationshavebestestimateαval-

|          | 10◦,         | α    |           |            |         |     |     |     |     |

| ues less | than and two | have | estimates | just a few | degrees |     |     |     |     |
higher.Onlytwoofthesimulationshaveanoptimumαestimate
| anywherenear                | the circle | size α of   | the INC3 | observationalbest |     |     |     |     |     |

| estimategiveninTable5:αINC3 |            | =30.8◦(forP |          | =0.5).            |     |     |     |     |     |
min
Do the latter two simulations, which are similar to the ob- 0 0 0 10 10 10 20 20 20 30 30 30 40 40 40 50 50 50 60 60 60
α α α
servationalmapinthesensethatanoptimalsolutionawayfrom
sufficientlysimilar
| low α limit       | is found,have |               |               | characteristicsto |        |                     |                     |           |                    |

|                   |               |               |               |                   |        | Fig.9. Distribution | of α and φ states   | where P > | 0.5 in the MCMC    |
| the observational | map           | such that the | observational | map               | can be |                     |                     |           |                    |
|                   |               |               |               |                   |        | chains for thetwo   | simulatedthree-year | INCmaps   | withlowest S ξ es- |
consideredachancerealisationstatisticallysimilartothesetwo
timates(simulations92and90,intheupperandlowerpanelsrespec-
| simulations? | Figure 11 | does not support |     | this. The two | simula- |     |     |     |     |

tively).
| tions are | among the simulations | that | have | the highest | S ξ esti- |     |     |     |     |

mates, well above three times that present in the observational Table5.Estimatesofmatchedcircleradiusαandtwistphaseφforthe
map. This is consistent with what is expected:the stronger the INC3observationalmap.
auto-correlationonlargescales,thehigherthechanceisofget-
ting highcross-correlationsbetweenapparentlydistantpartsof
|     |     |     |     |     |     |     | Pa nb | α φ |     |

theskyoveralargenumberofpixelpairs,ratherthanescaping min ◦ ◦
tothelowαlimitwheretherearerelativelyfewpixelpairs.This
|     |     |     |     |     |     |     | 0.3 294.3 | 32.7 27.6 |     |

canbequantifiedasfollows.
|       |                     |                 |     |             |      |     | 0.4 197.2 | 30.8 31.2 |     |

| Since | the α distributions | are constrained |     | from below, | they |     |           |           |     |
|       |                     |                 |     |             |      |     | 0.5 108.8 | 30.8 32.5 |     |
areunlikelytobeGaussian.So,estimatingthesignificanceofthe
|                                  |     |                               |     |                  |          | a Minimumprobability;b | numberofMCMCstepscontributingtothe |     |     |

| correlationbetweenαandS          |     | amongthesimulationsisbestdone |     |                  |          |                        |                                    |     |     |
|                                  |     | ξ                             |     |                  |          | estimate.              |                                    |     |     |
| using a non-parametricstatistic. |     | Spearman’s                    |     | rank correlation | ρ        |                        |                                    |     |     |
| andKendall’srankcorrelationτ     |     | one-sidedtestswith            |     | a                | positive |                        |                                    |     |     |
correlationasthealternativehypothesisgiveprobabilitiesthatα
Dothetwosimulationswithhighαestimates(numbered58
24.5◦ 31.9◦
andS ξ areunrelatedof2.5%and2.4%respectively.Evenifwe and 80, with α estimates of and respectively)
arbitrarilyremovethetwosimulationswithhighαfromthedata have convergentestimates of dodecahedralface centresand φ?
set, the same two two rank correlation tests give probabilities Figure 12 indicates a poor convergence of dodecahedral face
thatαandS areunrelatedof12.6%and12.5%respectively. centres for simulation 58 and what looks like the superimpo-
ξ
This supports the visual impression from Fig. 11. For low sitionofastrongprimaryandaweaksecondaryconvergencein
S ξ ,an optimalcross-correlationin GRF simulationsshouldes- thecaseofsimulation80.Moreover,Fig.13showsthatbothof
capetothelowαlimit.Thepointrepresentingtheobservational thesetwosimulationshavequitestronglybimodaldistributions
simulationappearstobequiteexceptional. in φ rather than favouring any individual optimal value of the

| 666 |     | B.F.Roukemaetal.:Poincarédodecahedralspaceparameters |     |     |     |     |     |     |     |

100 
)ged( φ )ged( φ )ged( φ )ged( φ
0 0 0 0
−100 
|     | 5 5 5 5 10 10 10 10 15 15 15 15 | 20 20 20 20 25 25 25 25 | 30 30 30 30 35 35 35 35 | 40 40 40 40 |     |     |     |     |     |

α (deg) α (deg) α (deg) α (deg)
Fig.10.Mediancirclesizesα(seeSect.4.3.4)andtwistanglesφ(mean)
foreachof20simulations(emptycircles)andtheWMAPobservational
map(solidcircle,valuesgiveninTable5),analysedusingthestepswith
P>0.5(seeEqs.(25),(26)ofRBSG08).Ineachcase,the10000steps
following2000burn-instepsofeachof4MCMCchainsstartedatran-
dompointsinparameterspaceareconcatenatedforthisanalysis.
40 40
35 35
Fig.12.Fullskymapshowingtheoptimalorientationofdodecahedral
30 30
|     |     |     |     |     | face centresbased | on40000              | stepsin4MCMC          | chains,        | usingthetwo |

|     |     |     |     |     | simulated         | three-year INC       | maps with the highest | α estimates    | (simula-    |
|     |     |     |     |     | tions 58          | and 80, in the upper | and lower panels      | respectively), | and the     |
)ged( α )ged( α 25 25
kp2mask,showingfacecentresforwhichP>0.5.
20 20
Distributionoftheoptimaltwistphaseφ
4.3.5.
15 15
ItisclearinFig.10thatthesimulationsgiveadistributionofbest
estimatetwistanglesφdifferentfromtheuniformdistributionon
| 10 10 |     |     |     |     | [−π,π]describedinEqs.(12)and(13)ofRBSG08anddiscussed |                    |                         |                  |         |

|       |     |     |     |     | in Sect.                                             | 5.4 of that paper. | Figure 14 shows         | the distribution | as      |
|       | 5 5 |     |     |     | a histogram.                                         | A two-sided        | Kolomogorov-Smirnovtest |                  | between |
0 0 1000 1000 2000 2000 3000 3000 4000 4000 the distribution of the best estimates of φ from the 20 simula-
S [(µK)4] S [(µK)4] tionsandauniformdistributionon[−π,π]rejectsequalitywith
ξ ξ
P=0.01.Thevaluesofφforthesimulations,showninFigs.10
Fig.11.MediancirclesizesαasafunctionofS foreachofthe20sim- intherange(−100◦,+100◦),andmostlyseemto
|     |     |     | ξ   |     | and14,alllie |     |     |     |     |

ulations (emptycircles) andtheWMAPobservational map (solidcir- clusterevenclosertoφ=0.
cle),analysedusingthestepswithP>0.5.
Alikelyexplanationisthatthisisaconsequenceoftheanti-
correlationintheauto-correlationfunctionmeasuredinWMAP
different
|     |     |     |     |     | sky maps | at nearly antipodal | scales by | authors | using |

twistφ.ThisisquitedifferentbehaviourtothatinFig.8forthe differentmethods(Fig.16,Spergeletal.2003;Fig.1,RBSG08).
observationalmap.
|     |     |     |     |     | TheHinshawetal.(2007)C |     | valuesshouldimplicitlyincludethe |     |     |

l
However,inordertobeconservative,letussupposethatsim- informationthatthereisanantipodalanti-correlation.Estimates
ulations 58 and 80 convergewell enough in comparison to the ofthe auto-correlationsofthesimulationsconfirmthatananti-
observationalmapthatwecanconsiderthemtohaveconvergent correlationofabout−100(μK)2atφ = ±πispresent,sothatthe
| MCMCsolutionswithα(cid:13)αlimit |     | =5◦.Thisgivesusanestimate |     |     |     |     |     |     |     |

simulationscorrectlyreproducethischaracteristicoftheobser-
(cid:11) (cid:12) vational data. This anti-correlation implies that MCMC chains
| α(cid:13)αlimit | |S ≤3.9S | (cid:3)10%, |     |     |     |     |     |     |     |

P INC3 (11) should disfavour φ = ±π when correlating pairs on a matched
|     | ξ ξ |     |     |     |                                           |     |     |                |     |

|     |     |     |     |     | circle pair,and,hence,generallydisfavourφ |     |     | = ±πforpairson |     |
(cid:13) αlimit
whereα representstheeventofgettinganon-Poisson- “matchedannuli”.ThisisdiscussedfurtherinSect.5.3.2.
10◦
noise signal at least (the MCMC step size) away from the Since a uniform distribution on [−π,π] is clearly wrong,
lowerlimitofαlimit. a reasonable hypothesis must be made regarding the intrinsic,

|     |     |     |     | B.F.Roukemaetal.:Poincarédodecahedralspaceparameters |     |     |     |     |     |     |     | 667 |

|     | 0 0 0 |     |     |     |     |     |     | NN 44 |     |     |     |     |

φ φ φ


|     |     |     |     |     |     |     |     |     | −−110000 | 00 110000 |     |     |

φφ
|     | 0 0 0 10 10 10 | 20 20 20 | 30 30 30 | 40 40 40 | 50 50 50 | 60 60 60 |     |     |     |     |     |     |

α α α
F√ig.14.Histogramoftheoptimaltwistangleφ(showninFig.10),with
|     |     |     |     |     |     |     | N error bars, | together | with a | Gaussian distribution | of  | width 38.4◦, |

centredatzero(seeTable6).
100 100 100 Table6.Propertiesofthedistributionofbestestimatesofφfromthe20
simulations.
|     |     |     |     |     |     |     |     |     | P   | φa Pb   |     |     |

|     |     |     |     |     |     |     |     |     | min | rm s KS |     |     |
◦
0 0 0
| φ φ φ |     |     |     |     |     |     |     |     | 0.3 | 32.9 5.9%  |     |     |

|       |     |     |     |     |     |     |     |     | 0.4 | 38.5 13.1% |     |     |
|       |     |     |     |     |     |     |     |     | 0.5 | 38.4 32.8% |     |     |
aRootmeansquarewidthofthedistribution;btwo-sidedKolmogorov-

|     |     |     |     |     |     |     | Smirnovprobability                         |     | thatthesimulational | values | areconsistent | witha |

|     |     |     |     |     |     |     | Gaussiandistributioncentredonzero,ofwidthσ |     |                     |        | =φ .          |       |
φ rms
|     | 0 0 0 10 10 10 | 20 20 20 | 30 30 30 | 40 40 40 | 50 50 50 | 60 60 60 |     |     |     |     |     |     |

α α α
thatthisasymmetryissufficienttojustifyassuminganasymme-
| Fig.13. Distribution | of  | α and φ | states where | P   | > 0.5 in | the MCMC |     |     |     |     |     |     |

chains for the two simulated three-year INC maps withhighest α es- try in the expected distribution of φ. Moreover, the means and
timates(simulations58and80,intheupperandlowerpanelsrespec- standard errors in the mean for the three P thresholds are
min
tively). 12.8± 7.1◦, 14.4± 8.4◦, 12.1± 8.6◦ respectively, showing no
statisticallysignificantdifferencefromzero.
GivenaGaussiandistributioninφcentredonzerowithwidth
=
expected distribution of best estimates of φ. Given the numer- σ φ φ rms aslistedinTable6,theprobabilitythatφisasclose
to±π/5astheobservationalvalue(Table5)iscloseto+π/5is
| ical results | from the | simulational | analyses |     | and the | presence of |     |     |     |     |     |     |

the φ = ±π anticorrelation, which should favour φ away from 22%,12.8%,9.4%forP =0.3,0.4,0.5respectively,i.e.
min
±π
| and towardszero,we     |     | assume | a Gaussian                |     | distribution, | f(φ), |          |     |     |          |          |     |

| centredonφ=0withwidthσ |     |        |                           |     |               |       | (cid:13) |     |     | (cid:14) | (cid:15) |     |
|                        |     |        | estimatedbythermsofφinthe |     |               |       |          |     |     | (cid:14) |          |     |
φ min(|φ±π/5|)<|φINC3−π/5|(cid:14) (cid:14)S ≤3.9S INC3 (cid:3)22%.
| simulations. |     |     |     |     |     |     | P   |     |     | ξ   |     | (12) |

ξ
| TheparametersofthisdistributionfordifferentP |     |     |     |     |     | values, |     |     |     |     |     |     |

min
andtheKolmogorov-Smirnovprobabilitiesthatthesimulational
|     |     |     |     |     |     |     | Since the | values | φ are themselves | not | too far from | π/5, it |

values are consistent with a Gaussian distribution, are given in rms
= = is clearly not so improbablethat φ ≈ ±π/5, compared to what
| Table 6. | For the lower | thresholds, | P   |     | 0.3 and | P 0.4, |     |     |     |     |     |     |

m in m i n would be expected from a uniform distribution on [−π,π]. In
| the Gaussian | distribution | hypothesis |     | i s mildly | reject | e d by the |     |     |     |     |     |     |

Kolmogorov-Smirnovtest.Ifwe setthemeanandstandardde- otherwords,thissuggeststhatusingthepresentmethod,anesti-
viation of the Gaussian distribution to be the mean and stan- mateofφisnotasgoodadiscriminatorbetweenachancePDS-
likesignalandanintrinsic,physicalsignalasitwouldbeifthe
| dard deviation | of the | simulational | φ   | estimates, | then | the three |     |     |     |     |     |     |

= expected distribution were uniform on [−π,π], i.e. there is an-
| Kolmogorov-Smirnovprobabilities |     |     | for | P min | 0.3,0.4,0.5 | are |     |     |     |     |     |     |

=54%,84%,97%respectively.Thus,itisclearthatthedis- other topologicaldegeneracy(cf. Aurichet al. 2005a)in CMB
P
KS
| tributionsareconsistentwithGaussianityifweusetheestimated |     |     |     |     |     |     | all-skymaps. |     |     |     |     |     |

meansratherthanforcesymmetryaboutφ=0. On theotherhand,isit justa coincidencethatφ ∼ π/5?
rms
Couldtherebeareasonablejustificationforusinganon-zero InSect.5.3.2belowwediscussthisquestion.Itispossiblethat
mean φ? The only possible source of systematic asymmetry is the empirical C l spherical harmonic spectrum, even with ran-
that the noise simulationsfollow noise patternsin the observa- domisedphases,mayencodemorecosmictopologyinformation
tionaldata,whicharenotperfectlysymmetrical.Itisnotobvious thanmightnaivelybeexpected.

| 668 |     |     |     | B.F.Roukemaetal.:Poincarédodecahedralspaceparameters |     |     |     |     |     |     |     |     |     |     |     |

4.3.6. Probabilityofrejectingthesimplyconnected,infinite, independent.Hence,theprobabilityestimateinEq.(14)cannot
|                    | flatmodel       |     |                                  |     |     |             |     | (yet)beassumedtobevalid. |           |         |         |              |            |              |         |

|                    |                 |     |                                  |     |     |             |     | As                       | mentioned | above,  | Spergel | et           | al. (2003) | estimated    | that    |
| The                | analysesofthese |     | simulationsindicatethatthe       |     |     | requirement |     |                          |           |         |         |              |            |              |         |
|                    |                 |     |                                  |     |     |             |     | P(S (cid:3)              | SWMAP)    | ∼ 0.15% | for     | an infinite, |            | flat, cosmic | concor- |
|                    |                 |     |                                  |     |     |             |     | ξ                        | ξ         |         |         |              |            |              |         |
| fortheMCMCchainsto |                 |     | avoid“escaping”tothelowerlimitin |     |     |             |     |                          |           |         |         |              |            |              |         |
dancemodel,withafixedspectralindexofdensityperturbations.
circlesizeαgivesastrongerconstraintagainstthesimplycon-
|     |     |     |     |     |     |     |     | Efstathiou | (2004) | estimated | P(S | (cid:3) | SWMAP) | ∼ 3–12.5%. | The |

nected,infinite,flatmodelthantherequirementthatcouldpoten- ξ ξ
tiallyexcludethePDSmodel,i.e.therequirementthatφ≈±π/5. latter calculation reconstructs unobserved structure hidden be-
Letuswrite thePDS-like characteristicsoftheWMAPob- hindthegalacticmaskbyassumingasimplyconnectedmodel.
servationaldatawhichwehavetriedtoreproducebysimulations Forthepurposesoftestingthesimplyconnectedmodelhypoth-
esis,thisisinternallyconsistent.
asfollows.Thedata
Usingthesetwoestimatestowritetworespectiveestimates
(i) havealargescalecutoffinstructurestatistics; (cid:3)SINC3)≈P(S (cid:3)SWMAP),wehave
|      |                     |     |     |                 |     |               |     | ofP(S ξ  |     |     | ξ        |     |     |     |     |

|      |                     |     |     | (cid:13) αlimit | ≈   | +π/5whenusing |     |          | ξ   |     | ξ        |     |     |     |     |
| (ii) | yielda solutionwith |     | α   | andφ            |     |               |     | (cid:18) |     |     | (cid:19) |     |     |     |     |
the MCMC method for optimising the cross-correlation ξ C (cid:3)SINC3)∩ξWMAP =
P (S ξ
forthe“generalised”PDS. ξ(cid:11) C (cid:12) (cid:11) (cid:12)
|     |     |     |     |     |     |     |     |     | P   | S (cid:3)SINC3 | P   | ξWMAP|S | (cid:3)SINC3 |     | (15) |

|     |     |     |     |     |     |     |     |     |     | ξ ξ            |     | C       | ξ            | ξ   |      |
Rewritetheseas
(i) S (cid:3)SINC3; by the definition of conditional probability. Hence, from
|     | ξ ξ |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- 
Eq.(13),wehave
(ii) ξ yieldsα(cid:13)αlimitandmin(|φ±π/5|)<|φINC3−π/5|≤8.4◦,
|     | C   |     |     |     |     |     |     | (cid:18)(cid:11) |     | (cid:12) | (cid:19) |     |     |     |     |

|     |     |     |     |     |     |     |     | = (cid:3)SINC3   |     | ∩ξWMAP   |          |     |     |     |     |
where we use the “worst” estimate of φ from Table 5, i.e. φ P S ξ < 0.015%,
27.6◦,forP =0.3.Forconvenience,wewritetheseevenmore (cid:18)(cid:11) ξ (cid:12) C (cid:19)
|             | min |     |     |     |     |     |     | P S (cid:3)SINC3 |     | ∩ξWMAP | <   | 1.25% |     |     | (16) |

| compactlyas |     |     |     |     |     |     |     | ξ                | ξ   | C      |     |       |     |     |      |
(cid:3)S
(i) S INC3; forthelowerandhighestimatesofP(S (cid:3)S INC3)respectively.
|     | ξ ξ |     |     |     |     |     |     |     |     |     |     |     | ξ   | ξ   |     |
| --- | --- 
ξWMAP.
(ii) In otherwords, the simultaneousexistence of bothof these
C
twopropertiesoftheWMAPdata,oneagenericcharacteristicof
|     |     | ≈ INC3 |     | WMAP |     |     |     |     |     |     |     |     |     |     |     |

Since both S ξ S and ξ are present in the WMAP smalluniversemodelsandtheotherhighlyspecifictothePDS,
|     |     | ξ   |     | C   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- 
data, the probability of these two characteristics both occur- is unlikelywith aprobabilityofabout99.99%or99%depend-
ringinthesimplyconnected,infinite,flatmodelcanbewritten
|     |     |     |     |     |     |     |     | ing on | whether | the Spergel | et  | al. (2003) | or  | Efstathiou | (2004) |

P[(S ≈ S INC3)∩ξ WMAP].Fromtheresultsabove,inparticular (cid:3) WMAP)areused.Thisresultonlyrequires
|     | ξ   |     |     |     |     |     |     | estimatesof | P(S | ξ S |     |     |     |     |     |

|     | ξ   | C   |     |     |     |     |     |             |     | ξ   |     |     |     |     |     |
fromEqs.(11)and(12),wecanwrite a frequentist approach to probabilities. Bayesian modelling of
| (cid:11) |         |              | (cid:12) | (cid:16)          |     |          |          | priorbeliefsisnotinvoked. |     |     |     |     |     |     |     |

| P        | ξWMAP|S | (cid:3)SINC3 | =        | P α(cid:13)αlimit |     |          |          |                           |     |     |     |     |     |     |     |
|          | ξ       |              |          |                   | and |          |          |                           |     |     |     |     |     |     |     |
|          | C       | ξ            |          |                   |     | (cid:14) | (cid:14) |                           |     |     |     |     |     |     |     |
|          |         |              |          |                   |     | (cid:14) | (cid:14) |                           |     |     |     |     |     |     |     |
min(|φ±π/5|)<(cid:14)φINC3−π/5(cid:14)
|     |     |     |     |          |          |     |     | 5. Discussion |     |     |     |     |     |     |     |

|     |     |     |     | (cid:14) | (cid:17) |     |     |               |     |     |     |     |     |     |     |
(cid:14) (cid:14)
|     |     |     |     | (cid:14)S (cid:3)S | INC3     |     |          |                                          |     |     |     |     |     |     |     |

|     |     |     |     | ξ                  | ξ        |     |          | 5.1.Matchedannuliandcalculationalspeedup |     |     |     |     |     |     |     |
|     |     |     |     | (cid:13)           | (cid:14) |     | (cid:15) |                                          |     |     |     |     |     |     |     |
(cid:14)
(cid:14) The preselection method described in Sect. 3.1 leads to faster
|     |     |     | ≤   | P α(cid:13)αlimit | (cid:14)S | (cid:3)SINC3 | ,   |     |     |     |     |     |     |     |     |

ξ ξ calculation times by a factor of about 3–10 (Sect. 4.1). This is
|     |     |     |     | (cid:13) | (cid:14) |     | (cid:15) |     |     |     |     |     |     |     |     |

(cid:14)
≤ α(cid:13)αlimit (cid:14) (cid:3)3.9SINC3 by eliminating most calculations of pair separations for pairs
|     |     |     |     | P   | (cid:14)S |     | ,   |     |     |     |     |     |     |     |     |

ξ ξ which are not useful for the cross-correlation calculation. Is it
(cid:3) 10%. (13) possible to improvethis algorithmeven further?Given thatwe
haveEq.(5),thenumberofcalculationsrequiredforagivento-
Aretheprobabilitiesthatα (cid:13) αlimit andφ ≈ ±π/5independent tal number of pairs could, in principle, be reduced by another
ofoneanother,sothatinsteadoftheEq.(13),wecanwrite
smallfactorasfollows.
(cid:16)
|     |                 |     |     |     |     |     |     | Randomly |     | select a | point p | from | a uniform | distribution | on  |

|     | α(cid:13)αlimit |     |     |     |     |     |     |          |     |          |         | i    |           |              |     |
P and S2, considered to be the left-hand copy of the SLS in either
(cid:14) (cid:17) F ig s . 1 o r 2 . F o r e a ch o f th e 1 2 h o lo n o m y t r an sf o r m a ti o n s g
|     |     |     |     | (cid:14) (cid:14) |     |     |     |     |     |     |     |     |     |     | j   |

min(|φ±π/5|)<|φINC3−π/5| (cid:14)S (cid:3)SINC3 to a d ja c en t c o p ie s o f th e fu n da m e n ta l d o m ai n , ch e c k i f t h e a n-
ξ ξ
(cid:14)
(cid:14) g l e α i j o n th e S L S f r o m p i t o t h e d o d e c a h e d r a l f a c e c e n t re f o r g j
|     |     | (cid:14) |     |     |     |     |     |     | ≤   | ≤   |     |     |     |     |     |

= P( α(cid:13)αlimit (cid:14)S (cid:3)S INC3)× s a ti s fi e s α − α α + . I f t h is c o n s t ra i n t is s a t i s fi e d , t h e n c h o o s e
|     |     | ξ   | ξ   |     |     |     |     |     |     | i j |     |     |     |     |     |
| --- | --- 
(cid:16) (cid:14) (cid:17) a s e c o n d p o in t p (cid:15) r a n d o m l y f r o m a u n i f o r m d i s t r i b u ti o n o n th e
|     | min(|φ±π/5|)<|φINC3−π/5|(cid:14) |     |     |     | (cid:14) |     |     |     |     | i   |     |     |     |     |     |

P (cid:14)S (cid:3)SINC3 ≈2.2%,(14) circle defined by the intersection of the right-hand copy of the
|     |     |     |     |     | ξ   | ξ   |     |                                       |     |     |     |     |     |                |     |

|     |     |     |     |     |     |     |     | SLSinFigs.1or2andthe2-spherecentredat |     |     |     |     |     | p,havingradius |     |
i
| again | using | Eqs. (11) | and (12)? | Spearman’s | rank | correlation |     | ρ r 2 . |     |     |     |     |     |     |     |

(p,p(cid:15))
andKendall’srankcorrelationτone-sidedtestswheremin(|φ± By construction, all of the pairs selected in this
i i
π/5|) decreases as α increases as the alternative hypothesis way are at separation r , and should be statistically equiva-

both give probabilities that these two parameters are unrelated lent to generating a full set of pairs of which both members
S2
of7.9%.Atwo-sidedtestgives16%inbothcases.Whileneither are uniformly selected on and then selecting those whose
oftheserejectionsofthehypothesisthatthetwoparametersare separations are close to r . A loop over values of r will give
|     |     |     |     |     |     |     |     |     |     |     | 2   |     |     |     | 2   |
| --- | --- 
unrelatedishighlysignificant,theyarestrongenoughrejections cross-correlations over the desired range of separations. This
that it would premature to assume that the two parameters are construction would bring the calculation method closer to the

|     |     |     |     | B.F.Roukemaetal.:Poincarédodecahedralspaceparameters |     |     |     |     |     |     |     |     |     | 669 |

identifiedcirclesmethoditself,withthedifferencethatinsteadof
asignificantrejectionoftheinfiniteflatmodel.Isthereanyway
correlatingpointslyingpreciselyalongthecircles,points“near” to avoid this interpretation? Other properties of the cosmolog-
thecirclesarecorrelated. ical componentof the WMAP data, unlikely in the infinite flat
This raises the question of differences between using the model,havebeennotedbymanyauthors.Itisunlikelythatthese
differentpropertiesarestatisticallyfullyindependentofonean-
| present | method | and using | the identified |     | circles method | with |     |     |     |     |     |     |     |     |

differences
| “thickened” | circles. | The | most likely |     | between | these | other. |     |     |     |     |     |     |     |

twomethodswoulddependonhow“thickening”isdefinedand On the other hand, in this case we have a physically mo-
howoverlappingthickenedcirclesaredealtwith. tivated model, motivated from the most fundamentallevel: the
spatialsectionoftheUniverseisa3-manifold,i.e.itmusthave
| “Thickening” |     | would | require | a somewhat | arbitrary | choice |     |     |     |     |     |     |     |     |

of an averaging procedure. For example, a circle could be di- a “shape”.AsSchwarzschild(1900,1998)stated a little overa
videdintoequalangularintervalsandthickenedsothatindivid- century ago, that shape may well be multiply connectedrather
ual bands of the annulus are internally averaged to obtain the thansimplyconnected.
temperature fluctuation at that angular position around the cir- cutoff
|     |     |     |     |     |     |     | More | recently, | the | generic | predictions | of  | a   | in power |

cle/annulus.Alternatively,aGaussiansmoothingcouldbeused.
atlargescalesweremadewhenonlytheCOBEdatawereavail-
However,neitherofthesemethodswouldtake intoaccountthe able(Starobinsky1993;Stevensetal.1993).Theidentifiedcir-
factthatthecomovingspatialseparationofapairofpoints“bor- clesprinciple(Cornishetal.1998),ofwhichthepresentmethod
dering”oppositeregionsoftheannulusdoesnotchangelinearly isanextension,andthematchingofthePoincaréDodecahedral
as the width of the annulus increases. In contrast, the present Space hypothesisto the large scale lack of power and the esti-
|                                                       |     |     |     |     |     |     | matesofΩ | ∼1.01–1.02(Luminetetal.2003),werepublished |     |     |     |     |     |     |

| methodcalculatesandusesthespatialseparationsdirectly. |     |     |     |     |     |     |          | tot                                        |     |     |     |     |     |     |
The problemof overlappingthickened circlesfollowsfrom without the knowledge that the present version of the method,
thefactthattwelvepairsofannulionthe2-sphereintersecteach allowingfora“generalised”PDSofarbitrarytwistangle,would
othermanytimes.Thegreaterthe thicknessofthe annulus,the beappliedtotheWMAPdata.Itseemsphysicallyunreasonable,
therefore,nottocombinetheprobabilitiesofthedifferentsigns
greaterthenumberofrandomlyselectedpointsintheseintersec-
tions.Ifacorrelationstatisticiscalculatedovereachcirclesepa- ofcosmictopology.
ratelyandthenaveraged,thenpointswhicharemembersofthese Inthiscase,toarguethattheprobabilityinEq.(16)hasun-
intersections contribute several times (typically two or three) derestimated,eithertheSpergeletal.(2003)orEfstathiou(2004)
moretothefinalstatisticthanpointswhicharemembersofonly probabilityestimatesofalowS
ξ havetobeincreased,orthees-
oneannulus.Ifchancefluctuationsatsomepairsoftheseinter-
|     |     |     |     |     |     |     | timate of | the probability |     | of a | PDS-like | signal, | given | a low S ξ , |

sections happen to have high correlations or anti-correlations, (Eq.(13))hastobeincreased.Wehaveconservativelytakenthe
then the final statistic might be biased by these pairs, since it maximum probability estimate in Table 5 of Efstathiou (2004)
| would implicitly |     | assume | that the | pairs are | independent | of one | fortheformer. |     |     |     |     |     |     |     |

another,eventhoughthisisfalseinsomecases.
|     |     |     |     |     |     |     | For the | latter,we | haveconservativelyassumed |     |     |     | thatthe | two |

The use of numerical simulations should make this more simulationswith α (cid:13) αlimit havea signalgivenby theMCMC
of a problem of excessive noise rather than systematic bias. It method similar enough to the signal in the observational map
is difficult to see any simple way in which a method directly thatwecansetthisprobabilityatP(ξWMAP|S (cid:3)SINC3)≤ 10%.
|              |                |               |           |                |       |            |                 |     |                             |     | C   | ξ                | ξ   |     |

| based on     | the identified | circles       | principle | could          | avoid | this prob- |                 |     |                             |     |     |                  |     |     |
|              |                |               |           |                |       |            | To increasethis |     | probabilitysignificantly,it |     |     | wouldbenecessary |     |     |
| lem, whether | or             | not its final | effect    | is statistical | bias  | or rather  |                 |     |                             |     |     |                  |     |     |
toarguethatmanyormostofthesimulationshaveconvergence
an extrasourceof noise.For theSLS optimalcross-correlation characteristics,bestestimatesofα(cid:13)αlimitandbestestimatesof
method, this problem does not exist, since both points are se- φ ≈ ±π/5similartothosefortheobservationalmap.Giventhe
| lected uniformly |     | on S2 and | selected | afterwards | based | on their |     |     |     |     |     |     |     |     |

resultspresentedinSect.4.3,asystematicerrorofthissortable
spatialseparations(themethodaspresentedinRBSG08),orelse
tosatisfythisseemsunlikely.
preselectedinawaythatisequivalenttothis(thepresentpaper).
|     |     |     |     |     |     |     | On the | contrary, | Fig. | 11  | and the rank | correlation |     | statistics |

Hence, results from comparing a series of thickened circle (Sect. 4.3.4)favouringa positive correlationbetween α and S
ξ
pairsforarangeofthicknessestouseoftheSLSoptimalcross- suggestthatP(ξWMAP|S (cid:3)SINC3)issmallerthanwhatwehave
correlationmethodshouldbe expectedto be different,forboth C ξ ξ
|     |     |     |     |     |     |     | beenableto | estimatewith |     | asmallnumberofsimulations.This |     |     |     |     |

geometricalandstatisticalreasons.
|     |     |     |     |     |     |     | is consistent | with | what | was | argued in | RBSG08, | i.e. | that the |

lowertheamplitudeofthelarge-scaleauto-correlations,theless
5.2.Five-yearWMAPdata chancethereshouldbeofcross-correlationsoccurringintheab-
senceofaPDS-likesignalorforawrongorientationofthePDS
| Thefive-yearWMAPdata(Sect.4.2)givebestestimatesofthe |     |             |                    |     |     |           | model. |          |     |          |             |            |     |         |

| PDS modelsimilar                                     |     | to thosefor | thethree-yeardata. |     |     | Sincemost |        |          |     |          |             |            |     |         |
|                                                      |     |             |                    |     |     |           | This   | suggests | two | possible | alternative | approaches |     | to that |
oftheimprovementintheWMAPdataisatsmallangularscales,
|     |     |     |     |     |     |     | used here. | Either | we  | could | generate | simulations | so  | that most |

thisisunsurprising.
|     |     |     |     |     |     |     | of theset | ofsimulationshaveS |     |     | aboutaslowas |     | thatobserved |     |

ξ
|     |     |     |     |     |     |     | – with the | kp2 | cut – or | we could | generate | simulations |     | for the |

5.3.Simulations full uncut sky. However, both of these approaches have prob-
lems.Theproblemsinbothcasesarisefromthefactthatalarge
Giventheinfinite,flatmodelwithGRFasanullhypothesis,the amountof the largescale poweris estimated to lie close to the
probability that the observed WMAP data could be a random GalacticPlane,buttheestimatesofhowmuchthispowerisand
realisation of this model, i.e. that both a large-scale cutoff in ofhowpreciselywecanmeasurethedetailedfluctuationsclose
power and a specifically PDS-like signal appearin the WMAP totheGalacticPlanearehighlyuncertain.Forexample,Table4
data, is estimated in Eq. (16) as 0.015% or 1.25% depending shows that the estimates for S ξ for the five-yearILC and TOH
respectively on whether we use the Spergel et al. (2003) or mapsdifferbyonly10%whenthekp2cutisused,butdifferby
Efstathiou (2004) estimates of the former. This appears to be nearlyafactorof2forthefullsky.

| 670 |     |     |     |     | B.F.Roukemaetal.:Poincarédodecahedralspaceparameters |     |     |     |     |     |     |     |     |     |     |

C
| Suppose | that | we generate |     | simulations |     | so that | most of the |     |     |     |     |     |     |     |     |

A
set of simulations have S about as low as that observed, us- B
ξ
ing the kp2 cut. In this case, we implicitly assume that both φ
φ
| the extrapolations              |           | from    | outside           | of the                     | kp2         | cut to   | inside it, as |     |     |     |     |     |     |     |     |

| wellas thedirectestimatesforthe |           |         |                   | fullsky,vastlyoverestimate |             |          |               |     |     |     |     |     |     |     |     |
| the power                       | inside    | the kp2 | cut.              | For testing                | a           | multiply | connected     |     |     |     |     |     |     |     |     |
| model hypothesis,               |           | this    | could             | have some                  | validity    | given    | that the      |     |     |     |     |     |     |     |     |
| spherical                       | harmonics | are     | not statistically |                            | independent |          | from one      |     |     |     |     |     |     |     |     |
| another.                        | However,  | this    | is not            | the null                   | hypothesis  |          | that is to be |     |     |     |     |     |     |     |     |
Fig.15.SchematicdiagramshowingtwocirclesontheSLSonwhich
testedwiththesimulations.Theaimistotestthenullhypothesis cross-correlationistobeoptimised,fortwistφ=0.Thefluctuationsare
ofasimplyconnected,infinite,flatmodelwithGaussianrandom zeroeverywhereonthetwocirclesexceptatthepointsAandBonthe
fluctuations. This model implies a relation between structures firstcircleandConthesecondcircle.Atallthreepointsthefluctuation
amplitudeis+1.
| inside and         | outside | of the | kp2  | cut, which   | needs | to       | be included |     |     |     |     |     |     |     |     |

| in the simulations |         | if we  | wish | to correctly |       | test the | hypothesis. |     |     |     |     |     |     |     |     |
Inotherwords,thestatistics offluctuationsgeneratedbysimu- simulationalmapsforthemainINC3analysis,wecarriedout12
S
lations which are designed to mostly have small ξ outside of additionalMCMCchainsontherealINC3mapinordertocreate
thekp2cutareunlikelytobestatisticallyequivalenttothoseof ahistogramequivalenttothoseinFig.5.Theresultinghistogram
fluctuationsgeneratedinthewayperformedhere.Inthepresent oftheφdistributionfromthe16chainsisshowninFig.16.This
work,thefullsetofsimulationswasgeneratedbytheHinshaw is clearly consistent with those in Fig. 5, in the sense that the
etal.(2007)estimatesoftheC values,andasubsetofthesewas +π/5peakstronglydominatesoverthe−π/5peak.
l
| selectedwiththecriterionthatS |     |     |     | outsideofthekp2cutmustbe |     |     |     |                                                    |     |     |     |     |     |     |     |

|                               |     |     |     | ξ                        |     |     |     | IsitphysicallyreasonablethataPDSmodelwouldgiveboth |     |     |     |     |     |     |     |
−π/5and+π/5asvalidtwistangles,evenwhereonetwistgives
| ascloseaspossibletoS |     |     | ξ oftheobservationsoutsideofthekp2 |     |     |     |     |     |     |     |     |     |     |     |     |

differentmethodsof
cut. These two generatingsimulationsare a muchweakersignalthantheother?Atmostoneofthesecan
distinct. indicate the correct 3-manifoldof comoving space. A possible
The second alternative to the present method would be to explanationfor bothtwist anglesto be favouredin the MCMC
| generate | simulations | for | the full | uncut | sky, | and to | run MCMC |              |         |             |     |               |     |      |         |

|          |             |     |          |       |      |        |          | chains might | be that | the density |     | perturbations |     | went | through |
chains on both these and the observational map. However, be- some sort of resonance process during an early epoch. In that
causeoftheintrinsicdifficultyincorrectingforemissioninthe
case,itisconceivablethataharmoniccreatedatthatearlyepoch
Galactic Plane and as is indicated in Table 4 for two different wouldstillremainpresent.Theoptimalcross-correlationsinthe
versions of the all-sky map of the cosmological signal, there simulations, in particular those shown in Figs. 9 and 13, also
| would then | be a | much | greatersystematic |     | uncertaintyin |     | the re- |              |               |     |           |        |     |              |     |

|            |      |      |                   |     |               |     |         | have bimodal | distributions | of  | preferred | values | of  | φ. Moreover, |     |
sults.Hence,bothofthesetwoalternativeapproacheshavedis- they appearto give nearly equalweightto solutions with posi-
advantagesrelativetothemethodusedhere. tive and negativevaluesofφ ofaboutthe same absolutevalue.
In addition to our main results of probability estimates, it This suggests that some type of pattern in the fluctuations can
has become clear that the properties of the expected distribu- tend to cause an MCMC chain to favour regions of φ approxi-
tion of φ (for the null hypothesisof an infinite, flat model) are matelysymmetricaroundzero.
notsimple.Thiscanbeunderstoodgenericallybyrealisingthat Thefollowingschematicdiagramshowsthatatleastonespe-
the mathematical procedure we are using is pattern matching. cificpatternoffluctuationsontheskycanleadtosomedegreeof
A cross-correlation for the correct mapping between two gen- symmetryofoptimalφvalues,totheextenttowhichthereal(or
uinelycorrelatedcopiesofasinglepatternwillnecessarilyyield simulated)patternmimicstheidealisedpattern.Figure15shows
| a highvalue. | However,for |     | a   | pattern | which | is sufficientlycom- |     |     |     |     |     |     |     |     |     |

twocirclesonoppositesidesofthesky,seenbysomeoneexter-
plex, both cross-correlations for incorrect mappings between nalto the SLS, lookingapproximatelybutnotnearlyalongthe
two genuinely correlated copies of a single pattern, and also axisjoiningthetwocircles.Ifweapproximatethisregionofthe
cross-correlationsforarbitrarymappingsbetweentwouncorre- covering space S3 as an approximately flat region for intuitive
lated patterns may in some cases yield high values due to the simplicity, then the mapping corresponding to a “generalised”
complexitiesofthepatternsandchancecorrelations.Fromfirst holonomytransformationfromonecircletotheotherisatrans-
lationfollowedbyatwist.Ifthetwistiseither+φor−φ,thenthe
principles,modellingthisisunlikelytobesimple.Forthisrea-
son, simulations provide an algorithmic shortcut to estimating summedcross-correlationis1.Ifthetwistisanythingotherthan
the likely distribution of φ, given a certain family of patterns. ±φ, includingzero,then these two idealised circleswill have a
GaussianrandomfluctuationsfromagivenC spectrumareone zerocross-correlation.
l
| suchfamilyofpatterns.ForadifferentC |     |     |     |     | spectrumordifferent |     |     |     |     |     |     |     |     |     |     |

l The original identified circles principle, i.e. the present
statisticalpropertiesofthefluctuations,differentcharacteristics
|     |     |     |     |     |     |     |     | method in | the limit of | zero pair | separations, |     | would | imply | that |

of the expected distribution of φ may occur. Here we discuss both of these patterns are equally optimal. By extension, our
somecharacteristicsofinterest. present method will find the same result for this idealised pat-
tern.
TendencyofanMCMCchaintofavourregionsofφ This schematic situation is clearly highly simplified. Apart
5.3.1.
|     |     |     |     |     |     |     |     | from the | fact that the | fluctuation | patterns |     | are unlikely |     | to be as |

approximatelysymmetricaroundzero
|     |     |     |     |     |     |     |     | simple as | in Fig. 15, | here we | have | assumed | that | the | MCMC |

Figure8inRBSG08andFigs.4and8eachindicatethatinad- chainisfixedataparticularorientationontheskyandmatched
ditiontothemaincross-correlationsignal,thereisalsoanaddi- circlesize.Inreality,thechainsarefreetochangebothofthese.
Changingorientationand/orcirclesizewouldweakenthesym-
tional,weak,secondarysignalwithanapproximatelyequalbut
opposite value of φ. This is clear in Table 3 of RSBG08 and metryprovidedbythepatterninFig.15.Hence,tocalculatethe
Fig. 5 for the five-year ILC and TOH maps. Since only four relevance of this schematic pattern realistically from first prin-
MCMC chains were carried out for each of the INC3 real and ciples would be quite complex. However, given that we have

B.F.Roukemaetal.:Poincarédodecahedralspaceparameters 671
888000000 this anti-correlation at φ = π is approximately −100(μK)2 in
mostsimulations.
The MCMC chains are optimised to find positive cross-
666000000 correlations, not anti-correlations. Hence, it should, in fact, be
expected9thatoptimalcross-correlationsshouldclustertowards
φ=0andawayfromφ=π.
We testthiswith a toy modelas follows.The angularscale
NNN 444000000
abovewhichtheauto-correlationbecomesnegativeinFig.16of
Spergel et al. (2003) is acos(−0.9) = 154◦. To first order, we
can approximately think of this as antipodal pairs of 25◦ discs
222000000
on the sky being anti-correlated. So, we start with one of the
simulated maps and randomlyselect 50 antipodalpairs from a
uniformdistributiononthesky.Foreachantipodalpair,wecal-
000 culatethemeantemperaturefluctuationwithin10◦ofeachpole.
−−−111000000 000 111000000 We choose this radius to be smaller than 25◦ so that there is a
φφφ
fairchancethatthediscweusewillmostlycoverasingle“anti-
Fig.16. Distributionof thetwist angle φ in16 MCMC chains run on correlated”disc,offullsize 25◦.Ifwe hadchosenthefulldisc
theINC3observationalmap,forstateswhereP> 0.5(t√hefourchains size,thenfrequentlytherewouldbetoolittleoverlapforananti-
showninFig.8plus12additionalMCMCchains),with Nerrorbars, correlationtobemeasured.Iftheproductofthemeantempera-
excludingstateswithα≤15◦.
turefluctuationsinthetwodiscsofthepairisnegative,thenwe
multiplythefluctuationsinonememberofthepairby–1.This
C’ B’ is donefor all50 antipodaldisc pairs. Ifthere were nooverlap
A betweenthesediscs,thenthiswouldcoverabout80%ofthefull
sky.
While this procedureis not likely to give a valid statistical
π set of fluctuation patterns for testing the infinite, flat universe
hypothesis, it should be sufficient for qualitatively testing the
hypothesis that the anti-correlation is responsible for the con-
centrationoftheexpecteddistributionofφawayfromπandto-
A’ wardszero.Moreover,sincetheanti-correlationattheantipodes
B C
providessome contributionto S , this proceduredecreases the
ξ
Fig.17.SchematicdiagramoftwocirclesontheSLSfortwistφ = 0, minimum, mean, and median values of S ξ for the 20 simula-
illustratingthattheobservedanti-correlationatantipodalpointsonthe tions from 1170,2928,3071(μK)4 to 467,1494,1169(μK)4 re-
SLS corresponds to an anti-correlation at twist φ = π on the circles. spectively,i.e.byaboutafactoroftwo.Themaximumvalueof
Solid circles at points A–C indicate positive fluctuations, and hollow S increasesslightly,from3782to4012(μK)4.
ξ
circlesattheantipodalpointsA(cid:15)–C(cid:15)indicatenegativefluctuations.
Figure18showstheresultofsearchingforoptimalPDSso-
lutions using four MCMC chains per modified simulation, and
analysing the chains as before. The distribution of best φ esti-
realistic numericalsimulations(forthe infinite, flatmodel),we
matesisshowninFig.19.Severaleffectsoftheantipodalanti-
do have an illustration here of at least one basic pattern which correlationreversalarevisibleinthetwofigures.Firstly,several
couldleadtobestsolutionswhichareapproximatelysymmetric optimalcorrelationsoccurclose to the antipodes,i.e. at φ ∼ π.
in φ aroundtwo values±φ, even thoughonly one of these two Secondly,thechainswhichescapetoαlimithaveoptimalφvalues
valuesisthe“true”value(physicalorsimulated)ofthemap. spreadoverawiderrangethanwithoutthemodification.These
two effects are qualitativelyconsistent with the hypothesisthat
theantipodalanti-correlationplaysanimportantroleinconcen-
5.3.2. Propertiesofthedistributionofoptimalφvalues tratingtheexpectedφdistributionforaninfinite,flatmodelto-
wardszero.
Statistical properties of the distribution of optimal φ values AthirdeffectcanalsobeseeninFig.18;afairlylargenum-
found in the analyses of the simulations (Fig. 14) are different
ber of chains no longer escape to αlimit. Since we reverse the
from what was intuitively expected. Not only is the distribu-
fluctuationsignin oneelementofeachof50antipodalpairs,it
tion of φ not uniform on [−π,π], but it is moder(cid:20)at (cid:21) ely (cid:22) well fit isclearthatthisdoesnotonlyaffectantipodalcorrelations,itcan
by a Gaussian centredon φ = 0◦ of width σ φ ≡ φ2 ≈ π/5 alsocreatecorrelationsatseveraldifferentscales,whichdidnot
(Table 6). Why is the distribution of optimal φ values not uni- exist in the originalsimulation. This can create highly artifical
formon[−π,π]?Whyshouldσ beapproximatelyπ/5?
φ attractorsfortheMCMCchains.
Considerthetwistangleφ=π.Onmatchedcircles,thisrep- The combination of these effects does not yield a distribu-
resents pairsof antipodalpoints, independentlyof the matched tionofφwhichlooksuniformbyinspectionofFigs.18and19.
circlesizeα.Figure17illustratesthisschematically.Ingeneral, A Kolmogorov-Smirnovtwo-sided test comparingthe φ distri-
apairofpointsonapairofwould-bematchingcirclesaresepa- bution to a uniform distribution on [−π,π] yields a probability
ratedbyatwistφ(cid:16)γ,whereγistheangleontheSLSseparat-
of16%,i.e.thedistributionisonlymarginallyconsistentwitha
ingthepairofpoints.Theexceptionisthatφ = πwhenγ = π. uniformdistribution.Clearly,althoughthenon-uniformdistribu-
Thisseparationcorrespondstoaspatialgeodesicseparationbe- tion ofφ isclearlyinfluencedby theantipodalanti-correlation,
tweenthepairofpointsinthecoveringspaceS3of2r
SLS
. thelatteraloneisinsufficienttoexplainit.
Forantipodalpoints,ξ isslightlynegative(Fig.16,Spergel
A
etal.2003;Fig.1,RBSG08).Inthesimulationsanalysedhere, 9 ThisfactwasmissedinRBSG08.

| 672 |     | B.F.Roukemaetal.:Poincarédodecahedralspaceparameters |     |     |                                      |      |      |               |     |       |         |             |

|     |     |                                                      |     |     | the simulated                        | maps | must | statistically |     | allow | φ to be | at least as |
|     |     |                                                      |     |     | highas π/5,butdonotnecessarilyhaveto |      |      |               |     | allow | itto    | bemuch      |
higher.Sincetherandomphaseshavenowayoffavouringright-
|     |     |     |     |     | handed twists | over | left-handed |     | twists, | a distribution |     | centred at |

φ=0andincludingvaluesroughlyupto±π/5isconsistentwith
theinformationthatthesimulationsshouldstatisticallycontain.
However,thereasonwhythedistributiondoesnotextendtoop-
)ged( φ )ged( φ )ged( φ
|     |       |     |     |     | timaltwistswith|φ| |     | (cid:13) π/5remainsanopenquestionforfuture |     |     |     |     |     |

|     | 0 0 0 |     |     |     | work.              |     |                                            |     |     |     |     |     |
|     |       |     |     |     | 6. Conclusion      |     |                                            |     |     |     |     |     |

Byuseofsomesphericaltrigonometry,itispossibletospeedup
theMarkovChainMonteCarlocross-correlationmethodoftest-
ingacosmictopologyhypothesisdescribedinRBSG08byafac-
torofabout3–10.ThisisshowninFig.1andEq.(5).Thiscould,
|     | 5 5 5 10 10 10 | 15 15 15 20 20 20 25 25 25 | 30 30 30 35 35 35 | 40 40 40 |     |     |     |     |     |     |     |     |

inprinciple,makeitpracticaltomakecalculationsathigherres-
α (deg) α (deg) α (deg)
|     |     |     |     |     | olutionthanbefore.However,the |     |     |     | physicalinterpretationofthe |     |     |     |

calculationswouldbeambiguousbecauseofseveralsystematic
| Fig.18. Median | circle sizes | α and twist angles | φ (mean) | for each | of  |     |     |     |     |     |     |     |

effectslistedabove.
| the20simulations,analysedusingthestepswithP |     |     | > 0.5,modifiedas |     |     |     |     |     |     |     |     |     |

describedinSect.5.3.2byinvertingtheanti-correlationin50randomly Moreover, for low matched circle sizes and low maximum
selectedpairsof10◦radiusantipodalpatchesonthesky. pairseparations,useofEq.(5)canincreasethenumbersofpairs
|     |     |     |     |     | per separation | bin, | thereby | decreasing |              | the noise. | A   | further im- |

|     |     |     |     |     | provementin    | the  | method  | and        | the relation | between    |     | this method |

|     |     |     |     |     | as a test | of “matched | annuli” |     | and tests | of matched |     | circles are |

discussedaboveinSect.5.1.
|     |     |     |     |     | Applying | the | faster | method | to the | ILC | and TOH | versions |

oftheWMAPfive-yeardata,wefindlittlesignificantchangein
thebestestimateparametersforaPoincarédodecahedralspace
|     |       |     |     |     | model of                                              | the Universe, |     | compared | to  | those | given in | RBSG08. |

|     | NN 44 |     |     |     | Dependingontheminimumpseudo-probabilitylevelusedinthe |               |     |          |     |       |          |         |
MCMCchainsthatisusedforestimatingthetwistφ,theoptimal
valueofφisafewdegreeshigherandafewdegreeslowerthan
+36.0◦intheILCandTOHmapsrespectively(Table3).

Wealsoappliedthefastermethodtoasmallnumberofsim-
|     |     |     |     |     | ulated skies.                                            | The | WMAP       | observations |     | confirmed |         | the generic |

|     |     |     |     |     | cosmic topology                                          |     | prediction | (Starobinsky |     | 1993;     | Stevens | et al.      |
|     | 00  |     |     |     | 1993)ofacutoffinstructurestatisticssuchasthetemperature- |     |            |              |     |           |         |             |
−−110000 00 110000 temperaturefluctuationauto-correlationonlargeangularorspa-
φφ
|     |     |     |     |     | tial scales. | Here, we | estimated |     | the weakness |     | of the | large scale |

Fig.19.HistogramofφvaluesshowninFig.18.TheGaussiandistri- auto-correlations using a statistic S ξ (Eq. (2)) similar to that
butionshowninFig.14isreproducedhere. of Spergel et al. (2003). The low observed value of S im-
ξ
|     |     |     |     |     | plies that | cross-correlations |     | on  | these | scales | should | usually be |

weak,sothatMCMCchainsasusedhereshouldhavedifficulty
Giventhatthe observationalmapdoesincludean antipodal finding a region of parameter space with high optimal cross-
anti-correlation,and possibly other features contributing to the correlations.Hence,toconservativelytesttheinfinite,flat,con-
non-uniformexpected distribution of φ, to what degree should cordancemodelhypothesis,ontheassumptionthattherealob-
the optimalcross-correlationsfavour φ close to zero, and what servationshavealowvalueofS duetobeingasinglerealisation
ξ
shape should the distribution of φ take? For example, if σ as ofarandomprocess,weanalysedsimulatedskieswhichusethe
φ
definedaboveis estimated onthe interval(withoutperiodicity) Hinshaw et al. (2007) C estimates and randomised phases of
l
[−π,π),thenhowsmallshoulditbe?
|     |     |     |     |     | the sphericalharmonics.Theobservationalmapwascalculated |     |     |     |     |     |     |     |

Thesimulationsaregeneratedfromsphericalharmonicsus- from the three least contaminatedfrequencyWMAP bands, Q,
ingthesphericalharmonicmeancoefficientsC ofHinshawetal. V andW,andtheGaussianrandomfluctuationsimulationswere
l
(2007),obtainedfromtheWMAPdata,butwithrandomphases createdusinganequivalentanalysispipeline(Lew&Roukema
2008).
(andsimulatednoise).Wechoosethoseofthesimulationswith
thelowestS ξ estimates.Thesesimulationscontainmuchofthe Forsimulatedandobservedskieswiththekp2Galacticcut,
sameinformationthatisintheobservationaldataset.Afterall, these simulations using the Hinshaw et al. (2007)C estimates
l
thisisthepointofsimulations. generally yield overestimates of S for the cut sky. Since we
ξ
We know that the MCMC chains in the data with the cor- prefertoanalysethe cutskyinordertominimise galacticcon-
|     | =   | +π/5, |     |     |     | effects, |     |     |     |     |     |     |

rect phases favour φ and have an anti-correlation at tamination it was necessary to select those simulations
2r .Randomisingthephasesofthesphericalharmonicswhile withthelowestvaluesofS ξ ,sothatthesimulationswerestatis-
SLS
retaining the C values should yield many statistical properties tically as similar as possible to the observationsoutside of the
l
| that are | similar to that | of the map with | the correct | phases. So, | kp2cut. |     |     |     |     |     |     |     |

|            |         |                 |           | B.F.Roukemaetal.:Poincarédodecahedralspaceparameters |       |                   |     |                                          |     |     |     |     | 673 |

| The        | results | of running      | MCMC      | chains                                               | on    | the 20 simula-    |     | References                               |     |     |     |     |     |
| tions with | the     | lowest S        | estimates | from                                                 | among | 50 simulations    |     |                                          |     |     |     |     |     |
|            |         |                 | ξ         |                                                      |       |                   |     | Aurich,R.2008,class.Quant.Gra.,25,225017 |     |     |     |     |     |
| were that  | only    | two simulations |           | gave optimal                                         |       | cross-correlation |     |                                          |     |     |     |     |     |
Aurich,R.,Lustig,S.,&Steiner,F.2005a,Class.Quant.Gra.,22,3443
| solutions | which | did not | escape | to the | lower | limit in | circle |     |     |     |     |     |     |

Aurich,R.,Lustig,S.,&Steiner,F.2005b,Class.Quant.Gra.,22,2061
size α, where small number statistics favour fortuitous cross- Aurich,R.,Lustig,S.,&Steiner,F.2006,MNRAS,369,240
Caillerie,S.,Lachièze-Rey,M.,Luminet,J.-P.,etal.2007,A&A,476,691
correlations.Thisindicatesaconditionalprobabilityoffindinga
Cornish,N.J.,Spergel,D.N.,&Starkman,G.D.1998,Class.Quant.Gra.,15,
non-noisesolutionofabout10%(Eq.(11)).
2657
| The | distribution | of  | optimal | twists | φ from | the simulations |     |     |     |     |     |     |     |

Cornish,N.J.,Spergel,D.N.,Starkman,G.D.,&Komatsu,E.2004,Phys.Rev.
showed that despite the low value of S , the expecteddistribu- Lett.,92,201302
ξ
tionofφ inthe simulationswas notuniform.Instead,itiscon- Efstathiou,G.2004,MNRAS,348,885
sistentwithaGaussiandistributioncentrednearφ=0,ofwidth Gausmann,E.,Lehoucq,R.,Luminet,J.-P.,Uzan,J.-P.,&Weeks,J.2001,Class.
∼33–38◦.Possiblereasonsforthenatureofthisdistributionare Quant.Gra.,18,5155
Gundermann,J.2005,arXivpreprints[arXiv:astro-ph/0503014]
discussedabove,inSects.5.3.1and5.3.2. Hinshaw,G.,Spergel,D.N.,Verde,L.,etal.2003,ApJS,148,135
Assuming this numerical, Gaussian fit to the expected (for Hinshaw,G.,Nolta,M.R.,Bennett,C.L.,etal.2007,ApJS,170,288
an infinite,flat model)distributionofφ, andusingthe estimate Hinshaw,G.,Weiland,J.L.,Hill,R.S.,etal.2009,ApJS,inpress
[arXiv:0803.0732]
ofφobtainedfromtheobservationalmap(Table5)thatismost
Key,J.S.,Cornish,N.J.,Spergel,D.N.,&Starkman,G.D.2007,Phys.Rev.D,
| discrepantfromπ/5,wefoundthatφcouldbeexpectedtobeas |     |     |     |     |     |     |     | 75,084034 |     |     |     |     |     |

closeto±π/5astheobservationalvalueiscloseto+π/5witha
|     |     |     |     |     |     |     |     | Lambert, J. 1772, | Anmerkungen | und Zusätze | zur Entwerfung | der Land | und |

probabilityofabout22%(Eq.(12)). Himmelscharten. In Beiträge zum Gebrauche der Mathematik und deren
BothoftheseprobabilitiesareconditionalonS beinglow, Anwendung,pt.3,sec.6.(Englishtranslation:NotesandCommentsonthe
|              |     |         |        |           |            | ξ             |     | Composition | of Terrestrial | and Celestial Maps, | Ann Arbor, | University | of  |

| which itself | is  | unusual | for an | infinite, | flat model | (e.g. Spergel |     |             |                |                     |            |            |     |
Michigan1972)
etal.2003;Efstathiou2004).Hence,foraninfinite,flat,cosmic Lehoucq,R.,Weeks,J.,Uzan,J.-P.,Gausmann,E.,&Luminet,J.-P.2002,Class.
concordancemodelwithGaussianrandomfluctuations,wefind Quant.Gra.,19,4683
that comparing an observational map with simulational maps Lew,B.,&Roukema,B.F.2008,A&A,482,747
Luminet,J.,Weeks,J.R.,Riazuelo,A.,Lehoucq,R.,&Uzan,J.2003,Nature,
| gives an | estimate | of  | the chance | of finding |     | both (a) a | large |     |     |     |     |     |     |

425,593
| scale autocorrelationas |     |     | weak | as thatobserved,and |     | (b) a | PDS- |     |     |     |     |     |     |

Niarchou,A.,&Jaffe,A.2007,Phys.Rev.Lett.,99,081302
like, optimal cross-correlation signal similar to that observed Riazuelo,A.,Weeks,J.,Uzan,J.,Lehoucq,R.,&Luminet,J.2004,Phys.Rev.D,
| to be about | 0.015% | or  | 1.25% | for the | Spergel | et al. (2003) | or  | 69,103518 |     |     |     |     |     |

Roukema,B.F.,Lew,B.,Cechowska,M.,Marecki,A.,&Bajtlik,S.2004,A&A,
| Efstathiou(2004)estimatesoftheprobabilityoflowS |     |     |     |     |     | respec- |     |         |     |     |     |     |     |

|                                                 |     |     |     |     |     | ξ       |     | 423,821 |     |     |     |     |     |
tively(Eq.(16)).
Roukema,B.F.,Bulin´ski,Z.,Szaniewska,A.,&Gaudin,N.E.2008,A&A,486,

Acknowledgements. ThankyoutoBartosz Lewfornumerous helpful andin- Schwarzschild,K.1900,Vier.d.Astr.Gess,35,337
Schwarzschild,K.1998,Class.Quant.Gra.,15,2539
sightfulcomments,andtotheanonymousrefereewhoprovidedconstructiveand
thoughtfulrecommendations. UsageoftheNicolaus CopernicusAstronomical Spergel,D.N.,Verde,L.,Peiris,H.V.,etal.2003,ApJS,148,175
Center(Torun´)computerclusterisgratefullyacknowledged.Usewasmadeof Starobinsky,A.A.1993,J.Exper.Theor.Phys.Lett.,57,622
theWMAPdata(http://lambda.gsfc.nasa.gov/product/),oftheCentre Stevens,D.,Scott,D.,&Silk,J.1993,Phys.Rev.Lett.,71,20
deDonnées astronomiques deStrasbourg(http://cdsads.u-strasbg.fr), Tegmark, M.,deOliveira-Costa, A.,&Hamilton, A.2003,Phys.Rev.D,68,
123523
| of GNU | Octave | command-line, | high-level | numerical | computation |     | software |     |     |     |     |     |     |

(http://www.gnu.org/software/octave),theGNUprojectRenvironment Weeks,J.2001,TheShapeofSpace(2ndEd.)(Manhattan:MarcelDekker)
forstatisticalcomputingandgraphics(http://www.r-project.org/)andthe Weinberg,S.1972,Gravitation andcosmology:Principles andapplications of
plotutils
GNU plottingpackage. thegeneraltheoryofrelativity(NewYork:Wiley)

---
**Source PDF:** `2020_29_article.pdf`
