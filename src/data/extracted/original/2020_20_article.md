| Spatial | constraints |           |            | underlying |           |     | the retinal |     | mosaics | of  |

| two     | types       | of        | horizontal |            | cells     |     | in cat      | and | macaque |     |
|         |             | Stephen   | J.         | Eglen1,†,  | James     |     | C. T. Wong  | 1   |         |     |
|         |             | Revision: |            | 1.26       | September |     | 23, 2018    |     |         |     |
2102 guA 5  ]CN.oib-q[  1v6890.8021:viXra

| Cambridge       | Computational          |        | Biology   | Institute |             |     |         |     |     |     |

| Department      | for AppliedMathematics |        |           | and       | Theoretical |     | Physics |     |     |     |
| University      | of Cambridge           |        |           |           |             |     |         |     |     |     |
| Wilberforce     | Road,Cambridge         |        | CB30WA,UK |           |             |     |         |     |     |     |
| † Corresponding | author.                |        |           |           |             |     |         |     |     |     |
| Phone:          | +44 (0)1223            | 765761 |           |           |             |     |         |     |     |     |
Email: S.J.Eglen@damtp.cam.ac.uk
Postprint of VisualNeuroscience (2008)25:209–214. doi:10.1017/S0952523808080176
Abstract
Most types of retinal neurons are spatially positioned in non-random patterns, termed reti-
nal mosaics. Several developmental mechanisms are thought to be important in the forma-
tion of these mosaics. Most evidence to date suggests that homotypic constraints within a
type of neuron are dominant, and that heterotypic interactions between different types of
neuron are rare. In an analysis of macaque H1 and H2 horizontal cell mosaics, Wa¨ssleetal.
(2000)suggestedthatthehighregularityindexofthecombinedH1andH2mosaicmightbe
caused by heterotypic interactions during development. Here we use computer modelling
tosuggestthatthehighregularity indexofthecombinedH1andH2mosaicisaby-product
ofthe basicconstraint thattwoneurons cannotoccupy thesamespace. Thespatial arrange-
mentof type A andtype Bhorizontal cellsin catretina also follow thissame principle.
Key words
| horizontal | cells, retinal | mosaics, | minimaldistance |     |     | model. |     |     |     |     |

Introduction
A defining feature for a type of retinal neuron is whether all neurons of that type tile the
retina in non-random patterns, termed “retinal mosaics” (Cook, 1998). This definition can
alsohelpus,togetherwithotheranatomicalandphysiologicalproperties,determinewhether
a group of neurons should be classified as one type, or subdivided into several types. For
example, cat beta retinal ganglion cells (RGCs) are classed into two types, the on-centre
beta RGCs and the off-centre beta RGCs, partly because the mosaic of either the on- or off-
centreneuronsindependentlytilestheretinaandeachmosaicismuchmoreregularthanthe
combined mosaic of all beta RGCs(Wa¨ssle etal., 1981). Furthermore, both cross-correlation
analysisandmodellingsuggestthatthesetwotypesofneuronareindependentofeachother
in respect of positioning, as well as physiological function, and, hence, may develop inde-
pendently (Wa¨ssleetal., 1981; Eglenetal., 2005). By contrast, Wa¨ssleet al. (2000) reported
that for another pairof neuronal types, the H1 andH2 horizontal cellsin macaque:
One would expect the nearest-neighbor distance of the combined mosaic to be
smaller than that of the individual mosaics. The regularity index [defined in
Methods, below], however, is comparable, suggesting that the H1 and H2 cells
are not arrayed completely independently. It is possible, that some interaction
betweentheirmosaicsduringretinaldevelopmentcreatesthisoverall regularity.
(Wa¨ssle etal., 2000, p597)
In this report we use computer modelling to investigate whether the high regularity in-
dexof the combined mosaic ofH1 and H2neurons is aproduct oftype-specific interactions
betweenthe twotypes, orwhetheritcanbeaccounted forsimplybyanatomical constraints
resulting from the two cell types occupying the same layer. To generalise this question
slightly, and to evaluate more experimental data, we will compare the spatial patterning
of horizontal cellsin macaquewith cat(Wa¨ssle etal., 1978).
Methods
Data sets Three horizontal cell fields were analysed: fields A and B are from macaque
(A: unpublished data; B: Figure 7 of Wa¨ssle etal. (2000)); field C is from cat (Figure 12 of
Wa¨ssle etal. (1978)). To keep our notation concise (rather than claiming any equivalence of
neuronal types across species), we denote type B cat horizontal cells as “type 1”, and type
A horizontal cells as “type 2”, in line with previously-noted similarities of primate H1 and
other mammalian B cells (deLima etal., 2005). Fields were digitised, and the cell location
taken to be the centre of each soma. Figure 1 shows an example real field along with a
matching simulation, definednext.
Bivariate d model Wehavegeneralisedthed model(Galli-Resta etal.,1997)tosim-
min min
ulatethe positioningoftwoneuronalpopulationswithinonefield. Eachtypeofneuronhas
its own homotypic exclusion zone (d or d ), but furthermore there is a heterotypic exclu-
1 2
sion zone (d ) to potentially allow for exclusions between the two types of neuron. (The

subscript refers to an interaction between two types of neuron, whereas the subscript

used below refers to all neurons irrespective of type.) First, we count the number of
1+2
type 1 and type 2 neurons (n and n ), and simulate an area A of the same size as the real
1 2
field. To initialise the simulation, we randomly position n type 1 neurons and n type 2
1 2
neurons within A. Neurons are then repositioned randomly within the field subject to two
constraints: that the nearest neighbour of the same type is greater than some distance (d


Figure 1: Real and simulated horizontal cell mosaics. Left: real mosaic (field A). Right:
example simulation. Open circles denote H1 cells, filled circles denote H2 cells; cells drawn
assuming 10 µm diameter. Scale bar: 100 µm. The simulated mosaic shows a close pair
of H2 cells (halfway across, two-thirds up); such close pairs are rare but can occur when a
homotypic exclusion zone issmall.
for type 1 neurons, d for type 2 neurons), and that the nearest neighbour of the opposite

type is greater than some distance d . Each of the distances d ,d ,d is a random variable
12 1 2 12
drawnfromaNormaldistributionwithagivenmeanandstandarddeviation. Randomval-
ues lower than a lower limit (5 µm) are discarded, to prevent implausibly small or negative
d values. This birth and death process (Ripley, 1977; Eglen etal., 2005) is repeated many
min
times until convergence (typically aftereach neuron hasbeen moved ten times).
Null hypothesis Somata of both types of horizontal cell occupy the same stratum of the
inner nuclear layer (INL). (In this study, we ignore the small population of displaced hori-
zontal cells that may be present in the ganglion cell layer (Silveira etal., 1989; Wa¨ssleet al.,
2000).) Ournullhypothesisstatesthatthedevelopmentalinteractionsbetweenthetwotypes
of neuron that influence their positioning are limited to preventing somal overlap: any two
neurons, regardless of type, cannot come closer than some minimal distance. In the context
ofoursimulations,thisimpliesthattherangeofd shouldmatchtherangeoftypicalsomal

diameters ofthe two types ofneuron.
Parameter estimates To fit one field, the free parameters in the model are the mean and
standarddeviationofthethreeexclusionzones. Thehomotypicexclusionzones(d ,d )were
1 2
estimated first by fitting a univariate d model (Galli-Resta etal., 1997) separately to the
min
type 1 and type 2 neurons. The size of the heterotypic exclusion zone, d , was assumed to

beofthesameorderasthesomadiameterofthehorizontalcells,around10µm. Parameters
were fitted by systematic searching overa range of plausible values.
Assessing goodness of fit Two measures were used to quantitatively compare our model
against the real data, the regularity index (RI) and the K function. The RI is computed by


(µm2)
|     | field | n n    | width | × height |     | d (µm) | d (µm)    | d    | (µm)  |

|     |       | 1 2    |       |          |     | 1      | 2         | 12   |       |
|     | A     | 187 82 | 400   | × 402    |     | 22 ±   | 4 40 ± 10 | 11   | ± 3.0 |
|     | B     | 206 86 | 298   | × 300    |     | 21 ±   | 4 32 ±    | 8 12 | ± 2.5 |
|     |       |        |       | ×1194    |     | ±      | ±         |      | ±     |
|     | C     | 300 85 | 723   |          |     | 65     | 12 72     | 8 14 | 3.0   |
Table 1: Parameters for each d simulation. The numberof type 1and type 2 neurons (n ,
min 1
n ) and the field size matches the values from the real field. The diameter of each exclu-

sion zone (d , d , d ) is drawn from a Normal distribution, listed here as mean ± standard
1 2 12
deviation.
measuring the distance of each non-border neuron to its nearest-neighbour, and then di-
viding the mean of this distribution by its standard deviation (Wa¨ssle & Riemann, 1978).
(Nearest-neighbour distances of neurons at the border of a field are excluded as those dis-
tances are unreliable. A neuron is excluded if its Voronoi polygon touches the boundary of
the field. This exclusion criterion accounts for the small differences in RI between our work
and those previously reported.) We measure three RI values: RI (distance of each type 1

neurontonearesttype1neuron), RI : (likeRI ,butfortype2neurons),andRI : (distance
|         |           |              |         | 2            | 1   |          |     |     | 1+2 |

| of each | neuron to | nearestother | neuron, | irrespective |     | oftype). |     |     |     |
K(t)
For one population of neurons, measures the number of cell pairs within a given
distance t of each other (Ripley, 1976; Eglen etal., 2005). For plotting purposes, we show
L(t) = [K(t)/π]1/2. This transformation discriminates between exclusion (L(t) < t), clus-
tering (L(t) > t) andcomplete spatial randomness (L(t) = t). We measure four L functions:
L : pairs of type 1 neurons; L : pairs of type 2 neurons; L : pairs of neurons of either
| 1   |     |     | 2   |     |     |     | 1+2 |     |     |
| --- | --- 
type. Finally, L measures the cross-correlation, by constraining cell pairs such that one

cell is type 1 and the other is type 2. Full details of these measures are given elsewhere
| (Eglen et | al., 2003, | 2005). |     |     |     |     |     |     |     |

To quantitatively evaluate the goodness of fit of the model to the real data, each sim-
ulation was run 99 times with the same parameters, but from different initial conditions.
Informally, ifthemeasure from the realdata fallswithin the distribution ofobserved values
from the simulations, then the model fits the data. This can be quantified with a p value
using a Monte Carlo ranking test. A test statistic (T) is measured for the K function of the
i
realmosaic(i = 1)andforeachsimulatedmosaic(i = 2...100). Apvalueisthencalculated
bydividingtherank(smallestfirst)of T by100. Pvaluesgreaterthan0.95indicateasignif-

icant difference at the 5% level between model and data. Full details of the test statistic are
| given in | Eglenet | al.(2005). |     |     |     |     |     |     |     |

Computational modelling and analysis was performed in the R environment, using the
splancspackageandVoronoidomainsoftware(R DevelopmentCore Team,2007;Rowlingson &Diggle,
1993; Fortune, 1987), as well as custom-written routines. The code is available from the au-
| thors upon | request. |            |     |     |     |     |     |     |     |

| Results    | and      | Discussion |     |     |     |     |     |     |     |
Table 1 lists the parameters used for each bivariate d simulation. The homotypic exclu-
min
sion zones(d , d )were independentlyfitted to eachmosaic, whereastheheterotypic exclu-
1 2
sion zone (d ) was set to just prevent neurons of opposite type from occupying the same

space in the inner nuclear layer. (Mean values of d reported in Table 1 are slightly higher

than estimates of somal diameter, suggesting that both cell bodies and some initial portion
of the primary dendrites contributed to steric hindrance between neuronal types.) Figure 2
shows that for each field, the model generates mosaics that quantitatively match the real
mosaics, as assessed by both the RI and the L functions. In three (out of twelve) cases the


goodness offitpvalueisgreaterthan0.95,indicatingthatformallythere isasignificantdif-
ferencebetweendataandmodel. Twoofthesecasesconcernbothtype1andtype2neurons
from cat retina (field C). Discrepancies in these two cases are apparent over small distances
(less than 10 µm between neurons of opposite type), and may be due simply to difficulties
in reconstructing the position of pairs of opposite-type neurons that seem to overlap in the
field from the original publication (Figure 12 of Wa¨ssle etal., 1978). Small errors in deter-
miningneuronalpositionarelikelywhenconsideringtherelativesizeofindividualneurons
withthesizeofthesamplefield. Overall,however,theLfunctionsforthedatafitwithinthe
confidence intervals of the model, suggesting that any disagreements between model and
data are quite small.
Regularityofad mosaicisinfluencedbybothneuronaldensityandthedistributionof
min
exclusionzonediameters. Forbothmacaquefields,themedianRIishigherforthesimulated
type 1 mosaics than for the simulated type 2 mosaics; the opposite is true for the cat field
<
(p 0.001 in each of three cases, Wilcoxon rank sum test). The high RI of simulated cat
type 2 mosaics, matching the observed data, is due to the relatively low s.d. in the type
2 exclusion zone (Table 1); if this is increased (e.g. from 8 µm to 16 µm), the median RI

decreasesto 4.5 (data not shown), belowthat of the type 1 mosaics.
The RIof the combined type 1 and 2 mosaic (RI )in each of our fieldsistypically 3–5,
1+2
matching the values observed experimentally. At first glance, this might seem quite high,
especiallycomparedtoatheoreticalexpectedvalueofaround1.9forcells(ofinfinitesimally
smallsize)arranged randomly(Cook,1996). Ourmodeltellsusthatthishigh RIissimplya
by-product of superimposing two regular, but independent, mosaics with somal exclusion.
This conclusion can be supported in two ways. First, by setting d to zero, we eliminate

all heterotypic interactions. (This allows for neurons of opposite type to become arbitrarily
close to one another, which is of course not realistic, but allows us to specifically test the
impact of removing all heterotypic interactions.) Figure 3A shows that RI drops con-
1+2
siderably to a median of around 2.5, whereas the fits to RI and RI remain good. In this
1 2
case, since there is no positional constraint between opposite-type neurons, the L function
for the random simulations follows the theoretical expectation L (t) = t. The deviation

between real data and simulations is apparent up to at least 20 µm (Figure 3B), as observed
by the L function for the real curve dropping well below the confidence intervals from the
simulations.
The second line of evidence to explain the high RI of the combined (type 1 and type 2)
mosaic is suggested by examining the fraction, f, of the retinal area occupied by the cell
bodies. This can be estimated by f = ((n +n )πr2)/|A| where r = 5 µm is an estimate of
1 2
radius of a horizontal cell soma, n and n are the number of type 1 and type 2 horizontal
1 2
cells, and |A| is the area of the field. Table 2 shows that the fraction of occupancy (f) corre-
lates with the regularity of the combined mosaic (RI ). Furthermore, Table 2 also shows
1+2
that the mean number of trial cell positions rejected due to infringement of the heterotypic
constraint also correlates with the RI, even when normalised for the number of potential
pairwise heterotypic interactions. In this light, the cat and macaque mosaics are generated
by the same mechanism, and the lower regularity of the combined mosaic in cat is due to
the smallereffectof somal exclusion.
Our bivariate d model is open to criticisms of biological plausibility. As previously
min
noted, exclusion models show us that local interactions are sufficient to generate regular
patterns, but do not inform us on how these interactions are mediated (Galli-Restaet al.,
1997). Herewewouldsuggestthatthehomotypicexclusionzonesaremediatedbyhorizon-
talcellprocesses,perhapsdrivinglateralmigrationduringdevelopment(Reeseetal.,1999).
The heterotypic interactions however are simply the result of steric hindrance between cell
bodies andprimary dendrites.


|     |     | A   |     |     |     |     | B   |     |     | C   |     |     |     |
| --- | --- | --- | --- | --- | --- 
|     |     | 6   |     |     |     | 6   |     |     |     | 11  |     |     |     |
xedni ytiraluger

|     |     | 4   |     |     |     | 4   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- 

|     |     | 2   |          |     |     | 2   |          |       |     |     | 2        |     |     |

|     |     |     | 1        | 2   | 1+2 |     | 1        | 2     | 1+2 |     | 1        | 2   | 1+2 |
|     |     | 40  |          |     |     | 40  |          |       |     | 100 |          |     |     |
|     |     |     | p = 0.49 |     |     |     | p = 0.63 |       |     |     | p = 0.81 |     |     |
|     | L 1 | 20  |          |     |     | 20  |          |       |     | 50  |          |     |     |
|     |     | 0   |          |     |     | 0   |          |       |     |     | 0        |     |     |
|     |     |     | 0        | 20  | 40  |     | 0        | 20    | 40  |     | 0        | 50  | 100 |
|     |     | 60  |          |     |     | 60  |          |       |     | 120 |          |     |     |
|     |     |     | p = 0.92 |     |     |     | p = 0.75 |       |     |     | p = 0.75 |     |     |
|     |     | 40  |          |     |     | 40  |          |       |     |     |          |     |     |
|     | L 2 |     |          |     |     |     |          |       |     | 60  |          |     |     |
|     |     | 20  |          |     |     | 20  |          |       |     |     |          |     |     |
|     |     | 0   |          |     |     | 0   |          |       |     |     | 0        |     |     |
|     |     |     | 0 20     | 40  | 60  |     | 0        | 20 40 | 60  |     | 0        | 60  | 120 |
|     |     | 40  |          |     |     | 40  |          |       |     | 60  |          |     |     |
|     |     |     | p = 0.97 |     |     |     | p = 0.87 |       |     |     | p = 1.00 |     |     |

2+1
|     |     | 20  |     |     |     | 20  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- 
L

|     |     | 0   |          |     |     | 0   |          |     |     |     | 0        |     |     |

|     |     |     | 0        | 20  | 40  |     | 0        | 20  | 40  |     | 0 20     | 40  | 60  |
|     |     | 40  |          |     |     | 40  |          |     |     | 60  |          |     |     |
|     |     |     | p = 0.92 |     |     |     | p = 0.74 |     |     |     | p = 1.00 |     |     |

|     | 21  | 20  |     |     |     | 20  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- 
L

|     |     | 0   |             |     |     | 0   |             |     |     |     | 0           |     |     |

|     |     |     | 0           | 20  | 40  |     | 0           | 20  | 40  |     | 0 20        | 40  | 60  |
|     |     |     | distance (m | m)  |     |     | distance (m |     | m)  |     | distance (m |     | m)  |
Figure 2: (Colour online.) Goodness of fit between data and model. Each column compares
one field (A, B: macaque; C: cat) with simulations. In the regularity index (RI) plots, the
thickgreenlineindicatestheRIoftherealdataforeithertype1,type2,orall(1+2)neurons.
Black dots are RI values from 99 simulations, together with their median (thin black line).
For each of four L function plots for a field, the L function for the real mosaic is shown as
a solid green line and dashed black lines indicate 95% confidence intervals of simulations.
| The | p value | isthe | goodness |     | of fitbetween |     | model | anddata. |     |     |     |     |     |

| A   |     |     |     | B   |     |     |     |

| 6   |     |     |     | 40  |     |     |     |
xedni ytiraluger
p = 1.00

| 4   |     |     |     | 20  |     |     |     |

L
| 2   |     |     |     | 0   |     |     |     |

|     | 1   | 2   | 1+2 |     | 0   | 20  | 40  |
distance (m
m)
Figure 3: (Colour online.) Results of bivariate d simulation for field A with d = 0, and
|     |     |     |     | min |     |     | 12  |

other parameters aslisted in Table1. Resultsare presented asin Figure 2.
| field | RI  | f rejects |     | n =   | n ×n rejects | / n   |     |

|       | 1+2 |           |     | pairs | 1 2          | pairs |     |
| C     | 3.4 | 0.04 242± | 10  | 25500 |              | 0.01  |     |
| A     | 3.9 | 0.13 940± | 32  | 15334 |              | 0.06  |     |
7198±282
| B   | 4.9 | 0.26 |     | 17716 |     | 0.41 |     |

Table 2: Estimates of the fraction f of sample retinal area occupied by all horizontal cell
bodiesineachfieldandincidenceofheterotypicconstraintenforcement. Rowsaresortedin
order of increasing regularity index of the combined mosaic. The mean (± s.d.) number of
times (per sweep) that the heterotypic constraint was broken, rejects, was counted over 99
simulations. The final column shows the mean number of rejects divided by the number of
| pairs ofopposite | type neurons. |     |     |     |     |     |     |

In conclusion, results from our computational model suggest that the high RIsobserved
for combined H1 and H2 mosaics in macaque are simply a by-product of the two mosaics
being positioned in the same stratum of the INL; the mosaics may be developmentally in-
dependent in all other respects. This result agrees with our earlier work on beta RGCs
(Eglen et al., 2005), as well as other studies demonstrating a lack of spatial correlations be-
tween manypairsofretinal neuronal types(Mack,2007;Rockhill etal.,2000). Exceptionsto
this findingare rare (Kouyama &Marshak, 1997; Ahneltetal., 2000).
Acknowledgements Thanks to Prof. Heinz Wa¨ssle for providing the unpublished field,
labelled field A in this study, and to Prof. John Troy for critical reading of this manuscript.
JamesWongwassupported by anEPSRC studentship.
References
Ahnelt, P. K., Ferna¨ndez, E., Martinez, O., Bolea, J. A. & Ku¨bber-Heiss, A. (2000). Irregular
S-cone mosaicsin felidretinas. Spatial interaction with axonlesshorizontal cells, revealed
bycross correlation. Journal of the OpticalSociety of AmericaA 17,580–588.
Cook, J. E. (1996). Spatial properties of retinal mosaics: an empirical evaluation of some
existing measures. VisualNeuroscience13,15–30.
Cook, J.E.(1998). Gettingtogripswithneuronaldiversity. InChaulpa,L.M.&Finlay,B.L.,
eds., Developmentand organization of the retina. Plenum Press, pages91–120.
de Lima, S. M. A., Ahnelt, P. K., Carvalho, T. O., Silveira, J. S., Rocha, F. A. F., Saito, C. A.
& Silveira, L. C. L. (2005). Horizontal cells in the retina of a diurnal rodent, the agouti
Dasyproctaaguti. VisualNeuroscience22,707–720.
Eglen, S. J., Raven, M. A., Tamrazian, E. & Reese, B. E. (2003). Dopaminergic amacrine
cellsinthe innernuclearlayerandganglion cell layercomprise asingle functional retinal
mosaic. Journal of Comparative Neurology466,343–355.
Eglen, S. J., Diggle, P. J. & Troy, J. B. (2005). Homotypic constraints dominate positioning of
on-and off-centre beta retinal ganglion cells. VisualNeuroscience22, 859–871.
Fortune, S. J. (1987). A sweeplinealgorithm for Voronoi diagrams. Algorithmica2,153–172.
Galli-Resta, L., Resta, G., Tan, S.-S. & Reese, B. E. (1997). Mosaics of Islet-1-expressing
amacrine cells assembled by short-range cellular interactions. Journal of Neuroscience 17,
7831–7838.
Kouyama, N. & Marshak, D. W. (1997). The topographical relationship between two neu-
ronal mosaics in the short wavelength-sensitive system of the primate retina. Visual Neu-
roscience14,159–167.
Mack,A.F.(2007). Evidenceforacolumnarorganizationofcones,Mu¨llercells,andneurons
in the retina of a cichlid fish. Neuroscience144, 1004–1014.
R Development Core Team (2007). R: A Language and Environment for Statistical Computing.
RFoundation for Statistical Computing, Vienna,Austria. ISBN3-900051-07-0.
Reese, B. E., Necessary, B. D., Tam, P. P. L., Faulkner-Jones, B. & Tan, S.-S. (1999). Clonal
expansion and cell dispersion in the developing mouse retina. European Journal of Neuro-
science11, 2965–2978.


Ripley, B. D. (1976). The second-order analysis of stationary point processes. Journal of
AppliedProbability 13,255–266.
Ripley, B. D. (1977). Modelling spatial patterns (with discussion). Journal of the Royal Statis-
| ticalSociety | B 39,172–212. |     |     |

Rockhill,R.L.,Euler,T.&Masland,R.H.(2000). Spatialorderwithinbutnotbetweentypes
ofretinalneurons. ProceedingsoftheNationalAcademyofSciencesoftheU.S.A.97,2303–2307.
Rowlingson,B.S.&Diggle,P.J.(1993). Splancs: spatialpointpatternanalysiscodeinS-Plus.
| Computers | and Geosciences19, | 627–655. |     |

Silveira,L.C.L.,Yamada,E.S.&Picanc¸o-Diniz,C.W.(1989). Displacedhorizontalcellsand
biplexiform horizontal cellsin the mammalianretina. VisualNeuroscience3, 483–488.
Wa¨ssle, H. & Riemann, H. J. (1978). The mosaic of nerve cells in the mammalian retina.
| Proceedingsof | the Royal Society | of London | SeriesB 200,441–461. |

Wa¨ssle, H., Peichl, L. & Boycott, B. B. (1978). Topography of horizontal cells in the retina of
the domestic cat. Proceedingsof theRoyal Society of London SeriesB 203,269–291.
Wa¨ssle, H., Boycott, B. B. & Illing, R. B. (1981). Morphology and mosaic of on-beta and
off-beta cells in the cat retina and some functional considerations. Proceedings of the Royal
| Society | ofLondon SeriesB212, | 177–195. |     |

Wa¨ssle, H., Dacey, D. M., Haun, T., Haverkamp, S., Gru¨nert, U. & Boycott, B. B. (2000). The
mosaicofhorizontal cellsin the macaquemonkey retina: with acommenton biplexiform
| ganglion | cells. VisualNeuroscience17, |     | 591–608. |

---
**Source PDF:** `2020_20_article.pdf`
