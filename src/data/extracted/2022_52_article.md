Replication/Ecology
R E S C I E N C E C [Re] Reproductive pair correlations and the clustering of
organisms
CoraliePicoche1,ID,WilliamR.Young2,ID,andFredericBarraquand1,ID
1InstituteofMathematicsofBordeaux,CNRS&UniversityofBordeaux,Talence,France–2ScrippsInstitutionofOceanography,
UniversityofCaliforniaatSanDiego,LaJolla,California,USA
Editedby
PierredeBuylID
Introduction
Reviewedby
FrancescoTurciID
RajeshSinghID In the present work, we replicate the results of Young et al. 2001 “Reproductive pair
correlationsandtheclusteringoforganisms”[1],ananalysisoftheformationofaggreReceived gatesinanotherwisehomogeneousenvironmentmimickingmarinesmall‐scalehydro24August2021
dynamics. Usinganindividual‐basedmodelofindependent,random‐walkingparticles
Published (alsocalled“Brownianbugs”),theyshowthatreproductionbyfissioninaturbulent[2]
13May2022 andviscousflowleadstotheformationofelongatedclusters. Spatialpatternstherefore
departfromtheusual,homogeneoussolutionoftheadvection‐diffusion‐reactionequaDOI
tionforalargepopulation.
10.5281/zenodo.6546488
Duetotheirsize,phytoplanktonorganismsexperienceamostlyviscousenvironmentin
alaminarshearfield,withrandombuthomogeneouschangesindirectionsduetoturbulence[3, 4]. Reproductionandlimitedmovementofdaughtercells, whichoccurat
thephytoplanktonscale,interactwiththesehydrodynamicsprocessesandcanleadto
aggregates. Inthiscontext,abetterunderstandingoftheinteractionsbetweendemography and small‐scale hydrodynamics could provide further explanation for observed
spatialdistributionofphytoplanktonspecies,andperhapseventheircoexistence. This
motivatedustorevisitYoungetal. 2001[1].
InadditiontoreplicatingthenumericalandmathematicalresultsofYoungetal. 2001,
wealsowishedtopresentthemathematicalderivationsthatweremissingfromtheoriginalpaper,whichshouldmakethisreplicationarticlemoreaccessibletomostreaders,
especiallythosewithoutafluidmechanicsbackground.
Brownianbugmodel
TheBrownianbugmodelisdefinedasanindividual‐basedmodelincontinuousspace
and time, here presented in its 2D formulation. For efficient computer simulation, it
isimplementedindiscrete(tim)e[1]. Eachparticleischaracterizedbythevectorofits
x
Cartesiancoordinatesx = 1 anditsoriginalpositiononthey‐axisatt = 0(achild
x

particleinheritsthisattribute),thislastcharacteristicbeingusedonlyforrepresentation
purposes. SpaceisaL×Lsquarewithperiodicboundaryconditions. Eachtimestep,
ofdurationτ, isdividedintothreesubsteps: (1)demographicprocesses, (2)diffusion,
Copyright©2022C.Picoche,W.R.YoungandF.Barraquand,releasedunderaCreativeCommonsAttribution4.0Internationallicense.
CorrespondenceshouldbeaddressedtoCoraliePicoche(coralie.picoche@u-bordeaux.fr)
Theauthorshavedeclaredthatnocompetinginterestsexist.
Codeisavailableathttps://github.com/CoraliePicoche/brownian_bug_fluid/tree/main/code–DOI10.5281/zenodo.6546471..
Openpeerreviewisavailableathttps://github.com/ReScience/submissions/issues/58.
ReScienceC8.1(#3)–Picoche,YoungandBarraquand2022 1


and(3)advection.
Demographicprocessestakeplaceduringthefirstsubstep(1).Eachorganismhasafixed
probability(p)ofreproducing,dying(q),orremainingunchanged(1−p−q).
Whenan
individualreproduces,aneworganismappearsontopoftheparent. Inthefollowing,
| p   | = q = | 0.5. |           |     |              |               |     |        |           | x′(t) = | x(t)+ |

|     |       |      | Diffusion | is  | then modeled | as a Brownian |     | motion | (2), i.e. |         |       |
N(0,∆)
δx(t) where each component of δx(t) follows a Gaussian distribution where
D = ∆2
isthediffusivity. Thediscrete‐timeMarkovchainpresentedhereapproximates
2τ
the continuous‐time Brownian bug model, which can be thought of as a spatial birthdeath or branching process (described in the Supplementary Material), step (1) being
referredtoinYoungetal. [1]asaGalton‐Watsonprocess. Finally,(3)theturbulentflow
governingadvectivestirringfollowsthePierrehumbertrandommap[5].
|     |     |     |     |       | ′                    |     | ′         |     |     |     |     |

|     |     |     | x   | (t+τ) | = x (t)+(Uτ/2)cos[kx |     | (t)+ϕ(t)] |     |     |     | (1) |
|     |     |     | 1   |       | 1                    |     | 2         |     |     |     |     |
′
|     |     |     | x   | (t+τ) | = x (t)+(Uτ/2)cos[kx |     | (t+τ)+θ(t)] |     |     |     | (2) |

|     |     |     | 2   |       | 2                    |     | 1           |     |     |     |     |
whereϕ(t)andθ(t)arerandomphasesuniformlydistributedbetween0and2π,k = 2π/L
andU isthestretchingparameter.
|     |     |     |     |     |     |     |     |     | N = | 20,000 |     |

Unless otherwise specified, each simulation is initialized with 0 particles
uniformlydistributedina1×1squareandrunfor1000timesteps.
PairdensityfunctionG(r,t)
| ThepairdensityfunctionG(x |     |     |     |     | ,x ,t)isdefinedsothatG(x |     |     | ,x  | ,t)dA | dA             |     |

|                           |     |     |     |     | i j                      |     |     | i j |       | 1 2 istheprob‐ |     |
abilityoffindingapairofBrownianbugswithonememberintheareadA aroundx
|     |     |     |     |     |     |     |     |     |     | 1   | i   |
| --- | --- 
andtheotherintheareadA aroundx . G(r,t)isactuallycalledthepaircorrelation
|     |     |     |     |     | 2   | j   |     |     |     |     |     |
| --- | --- 
C2g(r,t)
functionin[1]. Theradialdensityfunctiong(r,t)isdefinedasG(x i ,x j ,t) =
| withr | =|x | −x  | |. Asthepaircorrelationdisappearswhenr |     |     |     |     | →∞,g |     | →1. |     |

|       |     | i   | j                                      |     |     |     |     |      |     |     |     |
DerivationofG(r,t)—AlldetailsofthederivationofG(r,t)aretobefoundintheSupple‐
| mentaryMaterial. |     |         | Wefinallyobtain: |      |                |     |     |      |     |          |     |

|                  |     |         |                  | (    | )              |     |     | (    | )   |          |     |
|                  | ∂G  |         |                  | ∂    | ∂G             |     |     | ∂    | ∂G  |          |     |
|                  |     | =2Dr1−d |                  | rd−1 | +2(λ−µ)G+γr1−d |     |     | rd+1 |     |          |     |
|                  |     |         |                  |      |                |     |     |      |     | +2λCδ(x) | (3) |
|                  | ∂t  |         | ∂r               |      | ∂r             |     |     | ∂r   | ∂r  |          |     |
wherexisthepositionoftheparticle,λisthebirthrateandµisthedeathrate.
Wefocusonthecased=2andλ=µ,whichmeansEq.3canbereducedto
|     |     |     |     |     | (    | )   | ( ) |     |     |     |     |

|     |     |     | ∂G  | 2D  | ∂ ∂G | γ ∂ | ∂G  |     |     |     |     |
r3
|     |     |     |     | =   | r       | +    |     | +2λCδ(x) |     |     | (4) |

|     |     |     | ∂t  |     | r ∂r ∂r | r ∂r | ∂r  |          |     |     |     |
Thevalueofγiscomputedfromsimulations(seeSupplementaryMaterial).
Analyticalsolutionwithadvection—CP and FB could only find the analytical solutions of
G(r,t)
with and without advection with the indications of WY. In the presence of ad‐
̸=
vection (γ 0), a steady‐state solution can be found; without advection, there is no
steady‐stateandthesolutionchangesthroughtime. Letusfirstexaminethesteady‐state
solution,givenby:
| ReScienceC8.1(#3)–Picoche,YoungandBarraquand2022 |     |     |     |     |     |     |     |     |     |     | 2   |
| ------------------------------------------------ | --- 


|      |      | (    | )    | (    | )   |             |     |      |     |

|      | 2D ∂ | ∂G   | γ    | ∂    | ∂G  |             |     |      |     |
|      |      | r    | +    | r3   |     | +2λCδ(x)    |     | = 0  |     |
|      | r ∂r | ∂r   | r ∂r |      | ∂r  |             |     |      |     |
|      | (    | (    | )    |      | (   | )           | )   |      |     |
|      | 2D   | ∂    | ∂G   | γ    | ∂   | ∂G          |     |      |     |
| ⇔2πr |      |      | r    | +    | r3  | +2λCδ(x)    |     | = 0  |     |
|      |      | r ∂r | ∂r   | r ∂r |     | ∂r          |     |      |     |
|      | (    | (    | )    |      | (   | ))          |     |      |     |
|      |      | ∂    | ∂G   | ∂    | ∂G  |             |     |      |     |
| ⇔2π  |      |      |      |      | r3  |             |     |      |     |
|      | 2D   | r    | +γ   |      |     | +2πr2λCδ(x) |     | = 0. | (5) |
|      |      | ∂r   | ∂r   | ∂r   | ∂r  |             |     |      |     |
WecanthenintegrateEq.5overasmallareacenteredonaparticle,withradiusρ. Let
usfirstnotethat
∫
|     |     | δ(x)d2x |     |     |     |     | =   | 1   |     |

R2
∫ ∫
|     |     | 2π  | ρ          |     |       |     |     |     |     |

|     | ⇔   |     | ′          | ′   | ′     |     |     |     |     |
|     |     |     | δ(r )δ(θ)r |     | dr dθ |     | =   | 1   |     |
|     |     | 0∫  | 0          |     |       |     |     |     |     |
ρ
|     |     |     | ′ ′    | ′   |     |     |     |     |     |

|     | ⇔2π |     | δ(x )r | dr  |     |     | =   | 1   | (6) |

wherex′
istheequivalentofxinpolarcoordinates. UsingEq.5and6,wecanintegrate
between0andρ,
|     |     |     |     |     |     | (      |           | )    |     |

|     |     |     |     |     |     |        | ∂G        | ∂G   |     |
|     |     |     | 0   | =   |     | 2π 2Dρ | +γρ3      | +2λC |     |
|     |     |     |     |     |     |        | ∂r        | ∂r   |     |
|     | ⇔   | ∂G  |     |     |     |        | − 1       | 2λC  |     |
|     |     |     |     | =   |     |        |           | .    | (7) |
|     |     | ∂r  |     |     |     |        | 2π2Dρ+γρ3 |      |     |
Eq.7cannowbeintegratedbetweenρand∞,knowingthatG(∞)=C2:
∫
|     |     |     |     |     | 1   | ∞   | 2λC |     |     |

C2−G(ρ)=−
|     |     |     |     |     |     |         | dr. |     | (8) |

|     |     |     |     |     | 2π  | 2Dr+γr3 |     |     |     |
ρ
∫
u′
Usingthevariablechangeu=2Dr+γr3,theintegralisequivalentto du.
u
|     |         |     |     |     |     | [     | (          | )]   |     |

|     |         |     |     |     |     | λC 1  |            | 2D ∞ |     |
|     | C2−G(ρ) |     |     |     | −   |       | log(γ)−log |      |     |
|     |         |     |     | =   |     |       |            | +γ   | (9) |
|     |         |     |     |     |     | 2π 4D |            | r2   |     |
ρ
|     |     |     |     |     |     |     | (   | )   |     |

2D+γρ2
| ⇔G(ρ) |     |     |     |     |     |     | λC  |     |      |

|       |     |     |     | =   |     |     | log | +C2 | (10) |
|       |     |     |     |     |     | 8πD | γρ2 |     |      |
=G/C2isdefinedas
Finally,thepaircorrelationfunctiong
|     |     |     |       |      |     | (      | )   |     |      |

|     |     |     |       |      | λ   | 2D+γr2 |     |     |      |
|     |     |     | g(r)= |      | log |        | +1. |     | (11) |
|     |     |     |       | 8πDC |     | γr2    |     |     |      |
Analyticalsolutionwithoutadvection—WhenU = 0,γ = 0andthereisnosteadysolution
in2D.WecangetbacktoEq.4:
|     |     |     |     |     | (   | )           |     |     |      |

|     |     |     | ∂G  | 2D  | ∂   | ∂G          |     |     |      |
|     |     |     |     | =   |     | r +2λCδ(x). |     |     | (12) |
|     |     |     | ∂t  | r   | ∂r  | ∂r          |     |     |      |
Assuminganisotropicenvironment(andswitchingtotheCartesiancoordinatesystem),
thismeans
| ReScienceC8.1(#3)–Picoche,YoungandBarraquand2022 |     |     |     |     |     |     |     |     | 3   |

∂G
|     |     |     |     | −2D∆G=2λCδ(x) |     |     |     |     |     | (13) |

∂t
where∆=∇2istheLaplacianoperator.
Wethereforehave
|                                        |     |     |     | LG(x,t)=2λCδ(x) |     |       |     |     |     | (14) |

| whereListhelineardifferentialoperator∂ |     |     |     |                 |     | −2D∆. |     |     |     |      |
t
WecanuseaGreen’sfunctionH,definedwithLH
=δ(x,t)=δ(x)δ(t).
∫
Bydefinition,weknowthatG(y) = H(y,s)2λCδ(s)ds(wherey = (x,t))isasolution
toEq.14.
∫ ∫
t
|     | G(x,t) |     | =   |     | 2λC |     | H(x−x | ′ ,t ′ )δ(x | ′ )d2x ′ dt ′ |     |

|     |        |     |     |     |     | R2  | 0     | ∫           |               |     |
t
|     | ⇔   |     | =   |     |     |     |     | 2λC H(x,t | ′ )dt ′ | (15) |

Eq.15canbeusedinEq.12:
|     | ( ∫ |          | )   |     |     |          |     | ∫          |            |      |

|     | ∂   | t        |     |     |     |          |     | t          |            |      |
|     | 2λC | H(x,t)dt | ′ ′ |     |     | = 2D2λC∆ |     | H(x,t)dt ′ | ′ +2λCδ(x) | (16) |
∂t
|     | ∫ ( 0 |     |     | )   |     |     |     | 0   |     |     |

t ∂H(x,t′)
|     |     |           |     | ′   | ′   |        |     |     |     |      |

| ⇔   |     | −2D∆H(x,t |     | )   | dt  | = δ(x) |     |     |     | (17) |
∂t′
∫0
t
| ⇔   | ′       | ′   |     |     |     |        |     |     |     |      |

|     | δ(x)δ(t | )dt |     |     |     | = δ(x) |     |     |     | (18) |

whichistrue.
| AsolutionfortheGreen’sfunctionusingL=∂ |     |     |     |     |     |     | −2D∆in2dimensionsis |     |     |     |

t
|     |     |     |         |     |       | (   |       | )   |     |      |

|     |     |     |         |     | 1     |     | −r2   |     |     |      |
|     |     |     | H(r,t)= |     |       | exp |       | .   |     | (19) |
|     |     |     |         |     | 4π2Dt |     | 4×2Dt |     |     |      |
G(r,t)canthenbecomputed:
|     |     |     |     |     |     |    | ( ) |     |     |     |

t
r2
E 1
|     |     |     |            |     |     |    | 8Dt′ |    |     |      |

|     |     |     | G(r,t)=2λC |     |     |     |      |     |     | (20) |
8Dπ

∫
whereE (x)= ∞ e− tdtistheexponentialintegral.UsingG(r,0)=C2andlim x→+∞E = 0
|     | 1   |     |     |     |     |     |     |     |     | 1   |
| --- 
|     |     | x t |     |     |     |     |     |     |     |     |
inEq.20,wefinallyobtain
|     |     |     |     |     |     | (   | )   |     |     |     |
| --- 
r2
|     |     |     |     |           |     | E 1 |     |     |     |      |

|     |     |     |     |           |     | 8Dt | +C2 |     |     |      |
|     |     |     |     | G(r,t)=λC |     |     |     |     |     | (21) |
4Dπ
|     |     |     |     |     |     | (   | )   |     |     |     |
| --- 
r2
E
|                                                  |     |     |     |          | λ   | 1   | 8Dt |     |     |      |

|                                                  |     |     |     | ⇔g(r,t)= |     |     | +1. |     |     | (22) |
|                                                  |     |     |     |          | C   | 4Dπ |     |     |     |      |
| ReScienceC8.1(#3)–Picoche,YoungandBarraquand2022 |     |     |     |          |     |     |     |     |     | 4    |


Results
WewereabletoreproducethethreefiguresofYoungetal. [1]highlightingthespatial
distributionsofBrownianbugs.
In Fig. 1, the model has been run without the advection component and we can see
theclumpingoforganismsduetoreproduction. InFig. 2a), themodelhasbeenrun
withoutitsdemographiccomponent,butwithadvectionanddiffusion,confirmingthat
hydrodynamics alone cannot ensure cluster formation, while in Fig. 2 b), advection,
diffusionanddemographyarepresent,inwhichcaseorganismsformelongatedaggregates.
Fig. 3provedmuchmorechallenging. RetrievingtheanalyticalsolutionsofEq.4was
difficult as there was no other equation than Eq. 3 in the original paper. We also encountered issues when computing the pair correlation functions on simulations: for
largevaluesofr/∆,weobservedzerovalues(absentpairs)ofthepcfwhenU =0. This
isasamplingeffectaspcfvaluesgetverylowforlargedistanceswithoutadvection,even
thoughwemultipliedthestudyareaby10toproduceFig. 3andcountersucheffects.
Despitethemissingvalues,wecanconfirmthatsimulatedandanalyticalpcfmatch(Fig.
3),withaslightunderestimationbythesimulations. Thenumericalpcfalsogotcloser
to1thantheanalyticalpredictionsforlargevaluesofr.
ReScienceC8.1(#3)–Picoche,YoungandBarraquand2022 5


Figure1. Distribution of Brownian bugs at different times in a simulation with ∆ = 10−3 and
U = 0: initialconditionswithaPoissonspatialdistribution(a),t = 100τ (b)andt = 1000τ (c).
Eachparticleisidentifiedbyacolorwhichcorrespondstotheinitialpositiononthey‐axisofits
ancestoratt=0.
ReScienceC8.1(#3)–Picoche,YoungandBarraquand2022 6


Figure2.DistributionofBrownianbugsinasimulationwithadvectionand∆=10−3,Uτ/2=0.1:
withoutdemographicprocessesatt=30τ (a),andwithdemographicprocessesatt=1000τ
(b).
Eachparticleisidentifiedbyacolorwhichcorrespondstotheinitialpositiononthey‐axisofits
ancestoratt=0.

80+e1
| 60+e1 |     | −2  |     |     |     |

)901 x( 1−)t,r(g
40+e1
1−)t,r(g
20+e1

00+e1
Ut/2=0
Ut/2=0.1
Ut/2=0.5
Ut/2=2.5
20−e1
|       | Analytical solution |             | 0   |       |     |

| 1e−01 | 1e+01               | 1e+03 1e+05 | 0 5 | 10 15 | 20  |
|       |                     | D           |     | D     |     |
|       |                     | r           |     | r     |     |
Logarithmic(a)andlinear(b)plotsofg(r,t)versusr/∆,with∆ = 10−7 andUτ/2 =
Figure3.
0,0.1,0.5,2.5att = 1000τ. Tocomputesimulation‐basedvaluesofg(r)withalargenumberof
wereplicatedthe1×1square10times,
| points(N | 0 = 200√,000)andavoidsamplingissues, |     |     |     | so  |

thatitslengthis 10whilekeepingL = 1andk = 2π/Lineq. 1and2. Solidlinesresultfrom
simulations,dottedlinescorrespondtoanalyticalsolutionsandthesolidgreylineindicatesthe
r−2scalingpredictedbyEq.3.
| ReScienceC8.1(#3)–Picoche,YoungandBarraquand2022 |     |     |     |     | 7   |

Discussion
WesuccessfullyreplicatedboththenumericalresultsandanalyticalsolutionsofYoung
etal. [1].Eventhoughstochasticitypreventsusfromreplicatingexactlythesamespatial
pointpatternsasthoseseenintheoriginalFig. 1andFig. 2,weconsideredthepatterns
tobecloseenoughtovalidatethereplication.Fig. 3wasalsoveryclosetotheoneshown
intheoriginalarticle,despiteaslightunderestimationofthepcfinsimulateddata.
The most challenging part of the replication was actually not to replicate the numericalresults,buttofindbacktheanalyticalexpressionofthepairdensityfunctionG(r,t)
dynamics from first principles. How to derive such dynamics was indeed briefly explainedinwordsintheoriginalarticle,butthemanyintermediatestepsinvolved(see
SupplementaryMaterial)maketheadditionalmathematicalderivationspresentedhere
worthwhileinouropinion. InadditiontoprovidingcriticalinformationtoCPandFB
regardinghowtoobtainthepaircorrelationdynamics,WYalsocommunicatedtherequiredmathematicalstepstofindbacktheanalyticalsolutionsforG(r,t)plottedinFig.
3. WehopethattheadditionalmaterialonthederivationofG(r,t)dynamics(asSupplementary Material) as well as the provided analytical solutions of such dynamics (now
presentedinthemaintext)willhelpreadersthroughboththeoriginalandreplication
articles.
The original article did not provide quantitative values exactly matching marine microbesecology;wethuswonderedaboutthetimeandspatialscalesthatcouldbeused
forarealisticphytoplanktonmodel. Thelengthofthesquareside,L,isdefinedroughly
astheKolmogorovscale[2], thescaleatwhichviscositystartsdominatingturbulence
(weuseL=1cmasanupperbound).Here,weconsiderkthesmallestwavenumbercorrespondingtothelargestlengthscaleL,i.e. k =2π/L. Thechosenlengthscaledefines
the Reynolds number which then allows to obtain U, the velocity difference between
twopointsseparatedbyadistanceL.
U
Re = (23)
kν
UL
⇒1 = (24)
2πν
2πν
⇔U = (25)
L
where ν = 10−6m2.s −1 is the kinematic viscosity for water. These numerical values
lead to U = 6.3×10−4m.s −1. Note that U is the speed in the frame of reference of
the small square area considered here, which might itself be embedded within larger
spatialstructures(e.g.,largeeddies)movingathigherspeedsintheoceanoranylarge
waterbody.
Todeterminethediffusivityofsmallorganisms,weusetheStokes‐Einsteinequation[6]:
RT 1
D = (26)
N 6πηa
A
whereR=8.314J.K −1.mol −1isthemolargasconstant,T =293Kisthetemperatureof
theenvironment,N =6.0225×1023isAvogadro’snumber,η =10−3m −1.kg.s −1 isthe
A
viscosityofwaterandaistheradiusoftheorganismconsidered. Weapplythisformula
tomicrophytoplanktonorganismsofdiameter50μm,keepingτ outsideoftheequation
fornow:
ReScienceC8.1(#3)–Picoche,YoungandBarraquand2022 8


√
∆ = 2Dτ (27)
√
RT τ
= (28)
N 3πηa
A
√
8.314×293 1 √
= τ (29)
6.0225×10233π×10−3×25×10−6
√
= 1.3×10 −7 τ m. (30)
Tocomputeτ,wecanconsideraphytoplanktondoublingrateof1d −1[7],whichmeans,
withp=0.5,thatτ =0.5d.
This leads to Uτ/2 ≈ 5.4×103cm.d −1 and ∆ ≈ 5×10−5 cm. These two values are
muchhigherthanthoseusedinFig. 3(0.1 < Uτ/2 < 2.5and∆ = 10−7). Athorough
discussionoftheparametersisthereforenecessarybeforeextrapolatingtheseresultsto
realphytoplanktonicsystems.
AstheBrownianbugmodeliscurrentlyfairlytheoreticalinits2Dformulation,alogical
nextstepwouldbetoconsidersimilardynamicsina3D‐model,whichwouldrenderthe
comparisontorealdataeasier. Usingactualconcentrationsofphytoplanktonicorganisms(e.g. diatoms),between103and106C/L,thiswouldleadto1to103organismsifwe
keptL=1cm. Wemightthereforeneedtoincreasethesizeoftheconsideredsquare,or
applythemodeltosmallbacteriaonly. Withaclosermatchbetweenfieldandsimulated
concentrations,themodelcouldprovideuswithabetterpictureofthelikelyfine‐scale
spatialstructureofphytoplanktonicpopulations.
Acknowledgements
WearegratefultoFrancescoTurciforcommentsandtoRajeshSinghfordetailedfeedbackandcodesuggestions.
References
1. W.R.Young,A.J.Roberts,andG.Stuhne.“Reproductivepaircorrelationsandtheclusteringoforganisms.”In:
Nature412.6844(2001),pp.328–331.DOI:10.1038/35085561.
2. H.TennekesandJ.L.Lumley.Afirstcourseinturbulence.MITpress,1972.
3. D.B.Dusenbery.Livingatmicroscale:theunexpectedphysicsofbeingsmall.HarvardUniversityPress,2009.
4. F. Peters and C. Marrasé. “Effects of turbulence on plankton: an overview of experimental evidence
and some theoretical considerations.” In: Marine Ecology Progress Series 205 (2000), pp. 291–306. DOI:
10.3354/meps205291.
5. R.Pierrehumbert.“Tracermicrostructureinthelarge-eddydominatedregime.”In:Chaos,Solitons&Fractals
4.6(1994),pp.1091–1110.DOI:10.1016/0960-0779(94)90139-2.
6. A.Einstein.“ÜberdievondermolekularkinetischenTheoriederWärmegeforderteBewegungvoninruhenden
FlüssigkeitensuspendiertenTeilchen.”In:Annalenderphysik4(1905).DOI:10.1002/andp.19053220806.
7. J.E.Bissinger,D.J.S.Montagnes,J.Harples,andD.Atkinson.“Predictingmarinephytoplanktonmaximum
growthratesfromtemperature:ImprovingontheEppleycurveusingquantileregression.”In:Limnologyand
Oceanography53.2(2008),pp.487–493.DOI:10.4319/lo.2008.53.2.0487.
ReScienceC8.1(#3)–Picoche,YoungandBarraquand2022 9


| Supplementary |     |     | Material |     |     |     |     |     |     |

DerivationofG(r,t)
Diffusionandbirth/deathprocesses—Inthissection,weaimtofindbackfromfirstprinciples Eq. 2 in Young et al. [1], i.e. Eq. 3 in our manuscript. We will first focus on the
diffusion and birth/death processes, corresponding to the evolution equation for the
pairdensity:
|     |     |     |         | (    | )                |     |     |     |     |

|     |     | ∂G  |         | ∂    | ∂G               |     |     |     |     |
|     |     |     | =2Dr1−d | rd−1 | +2(λ−µ)G+2λCδ(x) |     |     |     |     |
(31)
|     |     | ∂t  |     | ∂r  | ∂r  |     |     |     |     |

WefirstdefineanensembleofkidenticalBrownianbugsinad‐dimensionalspace. The
bugnumberpislocatedatx = [x ,x ,...x ]. Attimet,thespaceisdefinedby(a)the
|     |     |     |     | p 1 2 | d   |     |     |     |     |

number of Brownian bugs k and (b) the vector of their locations X = [x ,x ,...x ].
|     |     |     |     |     |     |     |     | k 1 | 2 k |

ThisisalsocalledtheFockspace[8].
TheprobabilitydistributionoverthestatespaceisgivenbythefunctionsP (X ,t)such
k k
that:
|     | P   | (X ,t)dX | =Pr{kbugs,withabugindx |     |     |     | ,abugindx | ,etc.} | (32) |

|     |     | k k      | k                      |     |     | 1   |           | 2      |      |
Asbugsareindistinguishable,wecanexchangex andx (permutationsymmetry):
|     |     |     |     |     | p   |     | q   |     |     |

P (x ,...,x ,...,x ,...,x ,t)=P (x ,...,x ,...,x ,...,x ,t) (33)
|     | k   | 1   | p   | q k | k   | 1   | q   | p k |     |

Thenormalizationis:
|     | ∫      |          | ∫   | ∫          |          | ∫   |      |              |      |

| P   | (t)+ P | (X ,t)dx | +   | P (X ,t)dx | dx +...+ |     | P (X | ,t)dX +...=1 |      |
| 0   |        | 1 1      | 1   | 2 2        | 1 2      |     | k    | k k          | (34) |
R2k
becausehavingk individualsa∫ttimetdefinesapartitionofthesamplespacefork =
P
0,1,2,.... Wedefineb (x,t) = (x,X k−1 ,t)dX k−1 ,i.e. b (x,t)dxistheprobability
|     |     |     | k   | k   |     |     | k   |     |     |

thattherearekbugsandbugnumber1isindx.
Thedensityofpointsisdefinedas:
∫
|     |     |     | ∑∞  |     | ∑∞  |     |     |     |     |

P
|     |     | ρ(x,t)= |     | kb (x,t)= | k   | (x,X | k−1 ,t)dX | k−1 | (35) |

|     |     |         |     | k         |     | k    |           |     |      |
|     |     |         | k=1 |           | k=1 |      |           |     |      |
Thepaircorrelationfunctionisthen:
∫
∑∞
|     |     | G(x,y,t)= |     | k(k−1) | P (x,y,X |     | ,t)dX |     | (36) |

|     |     |           |     |        | k        |     | k−2   | k−2 |      |
k=2
∫
P
Wedefinethetwoparti∑cledistributionfunctionsc (x,y,t)= (x,y,X k−2 ,t)dX k−2 .
|                   |     |     | ∞   |                  | k   |     | k   |     |     |

| NotethatG(x,y,t)= |     |     |     | k(k−1)c (x,y,t). |     |     |     |     |     |
|                   |     |     | k=2 | k                |     |     |     |     |     |
Proposition
| ReScienceC8.1(#3)–Picoche,YoungandBarraquand2022 |     |     |     |     |     |     |     |     | 10  |

Thetimederivativeofc
k isgivenby:
∂c
k(x,y,t)=D∇2c
|     | k   |     | (37a) |

∂t 2
−k(λ+µ)c
|          | k   |     | (37b) |

| +(k+1)µc | k+1 |     | (37c) |
(k−2)(k+1)
λ
| +2 δ(x−y)b | k−1 (x)+λ | c k−1 | (37d) |

| k          | k         |       |       |
ReScienceC8.1(#3)–Picoche,YoungandBarraquand2022 11


Proof
| WewritetheevolutionofP |     |     |     |     | (X ,t): |     |     |     |     |     |     |

|                        |     |     |     | k   | k       |     |     |     |     |     |     |
∂P
k =D∇2P
|     |     |     |     |     | k   | k   |     |     |     |     | (38a) |

∂t
|     |     |     |     | −k(λ+µ)P |     |     |     |     |     |     | (38b) |

∫k
P
|     |     |     |     | +(k+1)µ |     |     | k+1 (X | k ,y,t)dy |     |     | (38c) |

|     |     |     |     |         | ∑k  | ∑k  |        |           |     |     |       |
λ
|     |     |     |     |     |     |     |     | −x )P |          |     |       |

|     |     |     |     | +   |     |     | δ(x | k−1   | (X k|p,t | )   | (38d) |
|     |     |     |     |     | k   |     | p   | q     |          |     |       |
p=1q=1,q̸=p
| where∇2 |     | 2   | 2   |       | 2   | 2   |      |        |          |     |     |

|         |     | = ∂ | + ∂ | +...+ | ∂   | + ∂ | andX | k|p =X | withoutx | .   |     |
|         | k   | ∂ 2 | ∂ 2 |       | ∂ 2 | ∂ 2 |      |        | k        | p   |     |
|         |     | x1  | y1  |       | xk  | yk  |      |        |          |     |     |
Here,Eq.38aisthediffusionpartoftheprocess,Eq.38bcorrespondstotherateatwhich
realizationswithkbugsloseabugbymortalityorgainabugthroughbirth,Eq.38ccorrespondstotherateatwhichrealizationswithk+1bugsloseabug.Finally,arealization
withkbugscanalsobeproducedbyabirthinarealizationwithk−1bugs.
CombiningthetimederivativeofP
|     |     |     |     |     |     | k (X k | ,t)withthedefinitionofc |     |     | k ,weobtain: |     |

∫
|     |     | ∂c  | k(x,y,t)=D |     | ∇2  | P      |     |           |     |     |       |

|     |     |     |            |     |     | (x,y,X |     | k−2 ,t)dX | k−2 |     | (39a) |
|     |     | ∂t  |            |     |     | k k    |     |           |     |     |       |
∫
|     |     |     |     | −k(λ+µ) |     | P   | (x,y,X | ,t)dX |     |     | (39b) |

|     |     |     |     |         |     |     | k      | k−2   | k−2 |     |       |
∫
|     |     |     |     | +(k+1)µ |     | P   | (x,y,X |     | ,z,t)dX | dz  | (39c) |

|     |     |     |     |         |     |     | k+1    | k−2 |         | k−2 |       |
∫
|     |     |     |     |     | ∑k  | ∑k  |     |     |     |     |     |
| --- | --- 
λ
|     |     |     |     | +   |     |     | δ(x | −x )P | (X        | )dX |       |

|     |     |     |     |     |     |     |     | p q   | k−1 k|p,t | k−2 | (39d) |
k
p=1q=1,q̸=p
Wewilltreatonetermaftertheother.
Diffusionterm(39a)
|     |     | ∫    |          |     |       |     |      | ∫   |        |         |       |

|     |     | D ∇2 | P (x,y,X |     | ,t)dX |     | =D∇2 | P   | (x,y,X | ,t)dX   | (40a) |
|     |     |      | k k      |     | k−2   | k−2 |      | k   | k      | k−2 k−2 |       |
∫
|     |     |     |     |     |     |     | =D∇2 | P   | (x,y,X | ,t)dX   |       |

|     |     |     |     |     |     |     |      | 2   | k      | k−2 k−2 | (40b) |
=D∇2c
|     |     |     |     |     |     |     |     | k   |     |     | (40c) |

becausewealreadyintegrateoverk−2coordinates(andthusLaplaciansforthesecoordinatesarezero).
Secondterm(39b)
∫
|                                                  |     |     | k(λ+µ) |     | P (x,y,X |     | ,t)dX |     | =k(λ+µ)c |     | (41) |

|                                                  |     |     |        |     | k        |     | k−2   | k−2 |          | k   |      |
| ReScienceC8.1(#3)–Picoche,YoungandBarraquand2022 |     |     |        |     |          |     |       |     |          |     | 12   |


Deathterm(39c)
∫ ∫
(k+1)µ P k+1 (x,y,X k−2 ,z,t)dX k−2 dz =(k+1)µ P k+1 (x,y,X k−1 ,t)dX k−1
(42a)
=(k+1)µc (42b)
k+1
Birthterm(39d)
Inthissection,weassumex = x andy = x (thereasoningisthesamefordifferent
1 2
positionsofxandyduetopermutationsymmetry).
Wecandecomposethedoublesum,startingwithp=1.
∑k
δ(x 1 −x q )P k−1 (x 2 ,...,x k ,t)=δ(x 1 −x 2 )P k−1 (x 2 ,...,x k ,t) (43a)
q=2
+δ(x 1 −x 3 )P k−1 (x 2 ,...,x k ,t) (43b)
+... (43c)
+δ(x 1 −x k )P k−1 (x 2 ,...,x k ,t) (43d)
Weintegrateoverthelastk−2coordinates.
∫
∑k
δ(x 1 −x q )P k−1 (x 2 ,...,x k ,t)dx 3 ...dx k (44a)
∫ q=2
= δ(x 1 −x 2 )P k−1 (x 2 ,...,x k ,t)dx 3 ...dx k (44b)
∫
+ δ(x 1 −x 3 )P k−1 (x 2 ,...,x k ,t)dx 3 ...dx k +... (44c)
∫
+ δ(x 1 −x k )P k−1 (x 2 ,...,x k ,t)dx 3 ...dx k (44d)
whichleadsto
∫
∑k
δ(x 1 −x q )P k−1 (x 2 ,...,x k ,t)dx 3 ...dx k (45a)
q=2 ∫
=δ(x 1 −x 2 ) P k−1 (x 2 ,...,x k ,t)dx 3 ...dx k (45b)
∫
+ P k−1 (x 2 ,x 1 ,...,x k ,t)dx 4 ...dx k +... (45c)
∫
+ P k−1 (x 2 ,...,x 1 ,t)dx 3 ...dx 1 (45d)
∫
=δ(x 1 −x 2 ) P k−1 (x 2 ,...,x k ,t)dx 3 ...dx k (45e)
∫
+ P k−1 (x 1 ,x 2 ,X k−3 ,t)dX k−3 +... (45f)
∫
+ P k−1 (x 1 ,x 2 ,X k−3 ,t)dX k−3 (45g)
=δ(x 1 −x 2 )b k−1 (x 2 )+(k−2)c k−1 (45h)
ReScienceC8.1(#3)–Picoche,YoungandBarraquand2022 13


Bysymmetry,ifp=2,weobtainδ(x 1 −x 2 )b k−1 (x 1 )+(k−2)c k−1 .
Now,weneedtousep≥3.
∫
∑k
δ(x p −x q )P k−1 (x 1 ,...,x p−1 ,x p+1 ,...,x k ,t)dx 3 ...dx k (46a)
∫
q=1,q̸=p
= δ(x p −x 1 )P k−1 (x 1 ,...,x p−1 ,x p+1 ,...,x k ,t)dx 3 ...dx k (46b)
∫
+ δ(x p −x 2 )P k−1 (x 1 ,...,x p−1 ,x p+1 ,...,x k ,t)dx 3 ...dx k + (46c)
∫
+ δ(x p −x 3 )P k−1 (x 1 ,...,x p−1 ,x p+1 ,...,x k ,t)dx 3 ...dx k +... (46d)
∫
+ δ(x p −x k )P k−1 (x 1 ,...,x p−1 ,x p+1 ,...,x k ,t)dx 3 ...dx k (46e)
∫ ∫
= δ(x p −x 1 )dx p P k−1 (x 1 ,x 2 ,...,x p−1 ,x p+1 ,...,x k ,t)dx 3 ...dx p−1 dx p+1 ...dx k
(46f)
∫ ∫
+ δ(x p −x 2 )dx p P k−1 (x 1 ,x 2 ,...,x p−1 ,x p+1 ,...,x k ,t)dx 3 ...dx p−1 dx p+1 ...dx k
(46g)
∫
+ P k−1 (x 1 ,x 2 ,x p ,...,x p−1 ,x p+1 ,...,x k ,t)dx 4 ...dx k +... (46h)
∫
+ P k−1 (x 1 ,x 2 ,...,x p−1 ,x p+1 ,...,x p ,t)dx 3 ...dx k−1 (46i)
∫
=2 P k−1 (x 1 ,x 2 ,X k−3 ,t)dX k−3 (46j)
∫
+(k−3) P k−1 (x 1 ,x 2 ,X k−3 ,t)dX k−3 (46k)
=2c k−1 +(k−3)c k−1 (46l)
=(k−1)c k−1 (46m)
∑ ∑ ∫
Thus, k p=3 q̸=p δ(x p −x q )P k−1 (X k|p )dX k−2 =(k−2)(k−1)c k−1 .
Finally,thebirthtermis
( )
λ λ (k−2)(k+1)
k
2δ(x−y)b k−1 (x)+2(k−2)c k−1 +(k−2)(k−1)c k−1 =2
k
δ(x−y)b k−1 (x)+λ
k
c k−1
(47)
Combiningallterms,weobtaintheexpectedresult:
∂c
k(x,y,t)=D∇2c
(48a)
∂t 2 k
−k(λ+µ)c (48b)
k
+(k+1)µc (48c)
k+1
λ (k−2)(k+1)
+2
k
δ(x−y)b k−1 (x)+λ
k
c k−1 . (48d)
Proposition
Incartesiancoordinates,thepairdensityadmitsthefollowingevolutionequation:
ReScienceC8.1(#3)–Picoche,YoungandBarraquand2022 14


∂G
|     |     | (x,y,t)=D∇2G+2(λ−µ)G+2λδ(x−y)ρ(x). |     |     |     |     | (49) |

∂t
Proof
UsingthedefinitionofG(x,y,t)andEq.37a‐37d:
∑∞
∂G
|     | (x,y,t)= |     | k(k−1)D∇2c |     |     | ≡T1 | (50a) |

|     | ∂t       |     |            | 2 k |     |     |       |
k=2
∑∞
|     |     | −   | k(k−1)k(λ+µ)c |     |     | ≡T2 |     |

(50b)
k
k=2
∑∞
|     |     | +   | k(k−1)(k+1)µc |     |     | ≡T3 |       |

|     |     |     |               | k+1 |     |     | (50c) |
k=2
∑∞
λ
|     |     | +   | k(k−1)2 | δ(x−y)b | (x) | ≡T4 | (50d) |

k−1
k
k=2
|     |     | ∑∞  |         | (k−2)(k+1) |       |     |       |

|     |     |     | λk(k−1) |            |       | ≡T5 |       |
|     |     | +   |         |            | c k−1 |     | (50e) |
k
k=2
∑
∞
| T1 T1=D∇2 |       | k(k−1)c | =D∇2G |     |     |     |     |

|           | 2 k=2 |         | k     | 2 k |     |     |     |
T3
∑∞
|     | T3= | k(k−1)(k+1)µc |     |     |     |     |       |

|     |     |               |     | k+1 |     |     | (51a) |
k=2
∑∞
|     |     | ′−1)(k | ′−2)k | ′   |       | ′    |       |

|     | =   | (k     |       | µc  | withk | =k+1 | (51b) |
k′
k′=3
∑∞
|     |     | ′−1)(k | ′−2)k | ′     | ′        | ′−2=0 |       |

|     | =   | (k     |       | µc k′ | ifk =2,k |       | (51c) |
k′=2
T4
∑∞
|     | T4=2λδ(x−y) |     | (k−1)b |         |     |     |       |

|     |             |     |        | k−1 (x) |     |     | (52a) |
k=2
∑∞
|     | =2λδ(x−y) |     | k ′′ | b k′′(x) | withk | ′′ =k−1 | (52b) |

k′′=1
=2λδ(x−y)ρ(x)
(52c)
T5
∑∞
(k−2)(k+1)
k(k−1)
| T5=λ |     |     |     | c k−1 |     |     | (53a) |

k
k=2
∑∞
|     | =λ  | k ′′ (k ′′−1)(k | ′′ +2)c |     | withk | ′′ =k−1 | (53b) |

k′′
k′′=1
∑∞
|     |     | ′′ ′′−1)(k | ′′   |     | ′′       | ′′−1=0 |       |

|     | =λ  | k (k       | +2)c | k′′ | ifk =1,k |        | (53c) |
k′′=2
| ReScienceC8.1(#3)–Picoche,YoungandBarraquand2022 |     |     |     |     |     |     | 15  |

T2+T3+T5
∑∞
|           | −k(k−1)k(λ+µ)c |     | +(k−1)(k−2)kµc |     | +k(k−1)(k+2)λc |     |

| T2+T3+T5= |                |     | k              |     | k              | k   |
k=2
(54a)
∑∞
|     | = k(k−1)c | (−k(λ+µ)+(k−2)µ+(k+2)λ) |     |     |     | (54b) |

k
k=2
∑∞
|     | =2(λ−µ) | k(k−1)c |     |     |     |       |

|     |         |         | k   |     |     | (54c) |
k=2
=2(λ−µ)G
|                |                          | k   |     |     |     | (54d) |

| T1+T2+T3+T4+T5 | Combiningallterms,wehave |     |     |     |     |       |
∂G
|     |     | (x,y,t)=D∇2G |     |     |     | (55a) |

∂t
|     |     |     | +2(λ−µ)G |     |     | (55b) |

k
|     |     |     | +2λδ(x−y)ρ(x). |     |     | (55c) |

Advectionprocess—UsingtheKraichnanequations[9],weprovethat,takingonlyadvectionintoaccount:
|     |     |        | (    | )   |     |      |

|     |     | ∂G     | ∂    | ∂G  |     |      |
|     |     | =γr1−d | rd+1 |     | .   | (56) |
|     |     | ∂t     | ∂r   | ∂r  |     |      |
Letr(t)bethedistancebetweentwopointsasafunctionoftime,whichfollowsageometricBrownianmotion,andq(t)=log(r(t))/log(r(0)). KraichnandefinesQ(q)asthe
WehaveQ=rdG.
| probabilitydistributionofq. |     |     |     | FromKraichnan[9]andFokker‐Planck |     |     |

equations,weknowthat:
|     |     | ∂Q  | ∂2Q | ∂Q  |     |     |

−γd
|                                     |     | =γ  |                                |     |     | (57) |

|                                     |     | ∂t  | ∂q2                            | ∂q  |     |      |
| whereγisthestretchingparameter,i.e. |     |     | thediffusivityandγdisthedrift. |     |     |      |
Wehave:
∂Q ∂(rdG)∂r
|     |     | =   |       |     |     | (58a) |

|     |     | ∂q  | ∂r ∂q |     |     |       |
|     |     |     | (     | )   |     |       |
∂G
drd−1G+rd
|     |     | =r  |     |     |     | (58b) |

∂r
∂G
|     |     | =drdG+rd+1 |     | .   |     | (58c) |

∂r
Therefore,
|     |     | (   |     | )   |     |     |

∂2Q ∂ ∂(rdG)∂r
|     |     | =   |           |        |     | (59a) |

|     | ∂q2 | ∂q  | ∂r ∂q     |        |     |       |
|     |     |     | (         | )      |     |       |
|     |     | ∂   |           | ∂G     |     |       |
|     |     | =r  | drdG+rd+1 |        |     | (59b) |
|     |     | ∂r  |           | ∂r     |     |       |
|     |     |     | ( )       |        |     |       |
|     |     | ∂   | ∂G        | ∂(rdG) |     |       |
rd+1
|                                                  |     | =r  |     | +rd | .   | (59c) |

|                                                  |     | ∂r  | ∂r  | ∂r  |     |       |
| ReScienceC8.1(#3)–Picoche,YoungandBarraquand2022 |     |     |     |     |     | 16    |


UsingEq.57,
|     |        | (     |      | )    |        |        |     |       |

|     | ∂(rdG) |       |      |      | ∂(rdG) | ∂(rdG) |     |       |
|     |        | ∂     | ∂G   |      |        |        |     |       |
|     |        | =γr   | rd+1 | +γdr |        | −γdr   |     | (60a) |
|     | ∂t     | ∂r    | ∂r   |      | ∂r     | ∂r     |     |       |
|     |        | (     |      | )    |        |        |     |       |
|     |        | ∂G ∂  | ∂G   |      |        |        |     |       |
|     | rd     |       | rd+1 |      |        |        |     |       |
|     |        | =γr   |      |      |        |        |     | (60b) |
|     |        | ∂t ∂r | ∂r   |      |        |        |     |       |
( )
|     |     |        | ∂    | ∂G  |     |     |     |       |

|     |     | =γr1−d | rd+1 | .   |     |     |     | (60c) |
|     |     | ∂r     |      | ∂r  |     |     |     |       |
WritingEq.60cwithEq.31,weobtainEq.3.
Stretchingparameterγ
iscomputedwithsimulations,usingtheformular(t)∝exp(γdt)→ 1ln(r(t))=γtif
γ

d=2,withrtheseparationbetweenpairsofparticles. γisestimatedastheslopeof

⟨ln(r(t))⟩=f(t)

with⟨ln(r(t))⟩theaverageobtainedfrom800pairsofparticles.
∑800

|     |     | ∀t,⟨ln(r(t))⟩= |     |        | (t)−x |           |     |     |

|     |     |                |     | ln(r(x | 1,p   | 2,p (t))) |     |     |

p=1
| r(x | (t) − x | (t)) |     |     |     | 1p  | x   |     |

where 1p 2p is the distance between a particle at position 1p and its
counterpart2p,initializedwithr(0)=10−7∀p(seeFig.4forγestimates).
| ReScienceC8.1(#3)–Picoche,YoungandBarraquand2022 |     |     |     |     |     |     |     | 17  |

| Ut  | /2=0, g =−2.82e−15 |                                                                                                       | Ut /2=0.1, g | =0.0264 |

| l   |                    | lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll |              |         |
0.6−
840950.8−
| )r(gol |     | )r(gol |     |     |

0.7−
840950.8−
0.8−
llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
| 0 20 | 40 60 80 100     | 0   | 20 40        | 60 80 100 |

|      | t                |     |              | t         |
| Ut   | /2=0.5, g =0.506 |     | Ut /2=2.5, g | =2.43     |
|      | l                |     |              | l         |
l l
l
| 2−  | l   | 2−  |     | l   |

l
l
l
| )r(gol 4− | l   | )r(gol 4− | l   |     |

l
l
| 6− l |     |     |     |     |

| l    |     | 6−  |     |     |
l
| 8−  |                | 8−      |         |             |

| l   |                | l       |         |             |
| 0 2 | 4 6 8 10 12 14 | 0.0 0.5 | 1.0 1.5 | 2.0 2.5 3.0 |
|     | t              |         |         | t           |
Figure4.EstimatesofγfordifferentUτ/2.
References
8. D.A.BirchandW.R.Young.“Amasterequationforaspatialpopulationmodelwithpairinteractions.”In:Theo-
reticalPopulationBiology70.1(2006),pp.26–42.DOI:10.1016/j.tpb.2005.11.007.
9. R.H.Kraichnan.“Convectionofapassivescalarbyaquasi-uniformrandomstrainingfield.”In:J.FluidMech.
64.4(1974),pp.737–762.DOI:10.1017/S0022112074001881.
ReScienceC8.1(#3)–Picoche,YoungandBarraquand2022 18

---
**Source PDF:** `19d8d84ef48e.pdf` (2022_52_article.pdf)  
**URL:** https://zenodo.org/record/6546488/files/article.pdf
