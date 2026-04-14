R E S C I E N C E C

Replication / ecology
[Re] Biodiversity of plankton by species oscillations and
chaos

Guillaume Doyen1, ID , Coralie Picoche1, ID , and Frédéric Barraquand1, ID
1Institut de Mathématiques de Bordeaux (UMR 5251), University of Bordeaux, CNRS, Bordeaux INP, Talence, France

Edited by
Timothée Poisot ID

Reviewed by
Kim Cressman ID
Jurg W. Spaak ID

Received
09 September 2022

Published
13 December 2023

DOI
10.5281/zenodo.10371655

## 1 Introduction

In the present article, we replicate the results of Huisman & Weissing 1999 Biodiversity
of plankton by species oscillations and chaos [1], an attempt to resolve the paradox of the
plankton [2] with a nonlinear ordinary differential equation model based on resource
competition theory.

According to many mathematical models, the number of phytoplankton species in a single homogeneous medium cannot exceed the number of separate resources available
[3, 4, 5] if the dynamics converge to a stable fixed point. However, it is very common
to observe more species than easily identifiable resources in field conditions. This led
Hutchinson to formulate the paradox of the plankton [2]. Using numerical simulations
of their ODE model, Huisman & Weissing [1] showed that “supersaturated coexistence”
is possible, where more consumer species than resource items coexist through oscillations or chaos, induced by the interactions between consumers and resources. We
attempt here to check this finding.

In addition to the replication of the numerical results of Huisman and Weissing [1], in
order to evaluate the sensitivity to the exact parameters used, we also present two novel
numerical experiments inspired by follow‐up articles, Does “supersaturated coexistence”
resolve the “paradox of the plankton”? by Schippers et al. 2001 [6], and Towards a solu-
tion of the plankton paradox: the importance of physiology and life history by Huisman et
al. 2001 [7]. These articles suggested that supersaturated coexistence might be difficult
to obtain outside of the restricted parameter scenarios considered in the original article. Schippers et al. [6] assessed the sensitivity of diversity to parameter perturbations.
They did so changing parameters for one species at a time, concluding that supersaturated coexistence was unlikely, while Huisman et al. [7] showed how some trade‐offs
can make parameter combinations favourable to coexistence emerge (although most of
the scenarios they consider confirm the results of Schippers et al. [6]). Here, we further
consider mild perturbations of intrinsic population growth rates of all species at once
(though not necessarily in the same direction), a hypothesis which we deem coherent
with whole‐ecosystem perturbations. If supersaturated coexistence is a likely coexistence mechanism, small changes to population growth rates should not massively affect
the number of coexisting species.


Code is available at https://github.com/fbarraquand/supersaturated_coexistence..
Open peer review is available at https://github.com/ReScience/submissions/issues/66.




## 2 Model

We describe below the model of phytoplankton community dynamics of Huisman &
Weissing [1]. Let Ni and Rj respectively be the population density of species i and concentration of resource j, i ∈ [[1, n]] and j ∈ [[1, k]] with n and k the number of different
species and resources. The time derivatives of Ni and Rj are given by:

with parameters

dNi
dt
dRj
dt

= Ni(µi(R1, ..., Rk) − mi)

= D(Sj − Rj) −

n∑

i=1

cjiµi(R1, ..., Rk)Ni

mi the mortality rate of species i
D the system’s turnover rate
Sj the supply concentration of resource j
cji the content of resource j in species i
µi the growth rate of species i,

defined using the Monod equation and Liebig’s law of the minimum:

µi(R1, ..., Rk) = min
j∈[[1,k]]

(

)

.

riRj
Kji + Rj

(1)

(2)

(3)

The growth rates are defined using:

ri the maximum growth rate of species i
Kji the half‐saturation constant for resource j of species i.

In order to reproduce the results of Huisman & Weissing [1], the differential equations
were integrated using the deSolve [8] package in its 1.32 version in R [9] 4.2.0, using
the same parameter sets as in the original article.

Multiple simulations are performed and illustrated in the original article as well as here:
In Figure 1 a) and b), 3 species are competing for 3 resources, in c), 6 species are competing for 3 resources (supersaturation) and in d), 9 species are competing for 3 resources
(supersaturation again). In Figure 2, 5 species are competing for 3 resources. In Figure
3, 5 species are competing for 5 resources. In Figure 4, 12 species are competing for 5
resources. In Figure 2 and Figure 1 a), b) and for the bifurcation diagram of Figure 3, all
of the species are introduced at the same time in the simulation. In Figure 4 and Figure
1 c), d), the species were introduced sequentially. Huisman et al. [1] have provided the
starting times of each species introduction when needed, in addition to the parameters.

As Schippers et al. [6], we were wondering how and why the parameter sets were initially chosen, and if the results would remain the same for slightly different parameters.
Several simulations were made in Schippers et al. [6] and Huisman et al.’s response [7],
in order to evaluate how robust was supersaturated coexistence. In the same spirit, we
carried out some new numerical experiments with a slightly different perspective.




We chose to focus on evaluating the robustness of the last simulation of Huisman &
Weissing [1], displayed on Figure 4. We focused on perturbating the growth rate parameter, ri, denoted as µmax in the follow‐up articles [6, 7]. As changing only a single one of
the n intrinsic growth rates ri (as done earlier in the follow‐up articles [6, 7]) appeared a
little artificial to us, we chose to randomly perturb all of the n intrinsic growth rates ri at
once, as would typically do an ecosystem‐wide perturbation that is not directly related
to the modelled resources. Furthermore, it seems overall more realistic, as the literature supports the idea that growth rates may vary between species even in the absence
of perturbations [10]. In a first numerical experiment, we considered the exact same
invasion sequence as Huisman & Weissing [1]. In the second numerical experiment, we
started with the full set of species at once.

In order to conduct the numerical experiments proposed earlier, the method used to
plot the fourth Figure has been reused. The two experiments were conducted 500 times
each, with as many different parameter sets: the ri, originally all set to the value of 1,
were drawn according to a truncated normal distribution. The mean was µ = 1 and
the variance was σ = 0.1, corresponding to CV = 10%. The distribution was truncated
using µ ± 3σ, in other words ri values remain between 0.7 and 1.3 (and most values
are much closer to 1). This range of values remains consistent, and even conservative,
when compared to experimental values [10], where CVs can be larger. As we are trying
to challenge the robustness of the replicated simulation, we do not change any other
parameters: thus we only conduct the simulations for a duration of 10000 days, as the
original simulations. However, in order to easily visualise how biodiversity changes
over time, we also measure the number of extant species at the times used in the article
to introduce new species, i.e. after 1,000, 3,000 and 5,000 days.

## 3 Results

### 3.1 Reproduction

We were able to replicate the four figures of Huisman & Weissing [1], presented below.




Figure 1. Oscillations on three resources. a), Time course of the abundances of three species competing for three resources. b), The corresponding limit cycle. c), Small‐amplitude oscillations of
six species on three resources. d), Large‐amplitude oscillations of nine species on three resources.

Figure 2. Chaos on five resources. a) Time course of the abundances of five species competing for
five resources, b) The corresponding chaotic attractor. The trajectory is plotted for three of the
five species, from the period from t = 1, 000 to t = 2, 000 days, c) Time course of total community
biomass.


0501001502000102030405005k10k15k02040600100020003000010203040Time (days)Time (days)Time (days)Species abundancesSpecies abundancesSpecies abundancesa)b)c)d)05010015020025030002040600100200300050100150Time (days)Time (days)Species abundancesTotal biomassa)b)c)

Figure 3. Bifurcation diagram, for five species competing for five resources. a) All of the values
of species 1, plotted during the period from t = 2, 000 to t = 4, 000 days, as a function of the
half‐saturation constant K41. Part of a) is magnified in b). c) show the local minima and maxima
of species 1, plotted during the period from t= 2,000 to t=4,000 days, as a function of the halfsaturation constant K41. Part of c) is magnified in d).

The bifurcation diagram 3 caption did not seem to correspond to the actual Figure,
which seemed to display all of the points of the simulation between t = 2, 000 and
t = 4, 000 rather that only the local extrema as the legend of the original article suggested. We have therefore chosen to draw those two options.




Figure 4. Competitive chaos and the coexistence of twelve species on five resources. a) abundances
of species 1‐6, b) abundances of species 7‐12.

### 3.2 Additional numerical experiments

For the first numerical experiment, which introduces species sequentially as in the original simulation, the distribution of the number of extant species is displayed in Figure 5.

Figure 5. Percentages of simulations with x species present, or with observable supersaturated
coexistence, at different times of the simulation for the first experiment. 500 simulations have
been run in total and a species has been considered present if Ni > 0.001.


02k4k6k8k10k020406002k4k6k8k10k05101520Time (days)Time (days)Species abundancesSpecies abundancesa)b)0 species1 species2 species3 species4 species5 species6 species7 species8 species9 species10 species11 species12 speciesSupersaturated05101520253035After 1000 daysAfter 3000 daysAfter 5000 daysAfter 10000 daysPercentage of simulations

These percentages show that the persistence of five species or more is very unlikely, and
that supersaturated coexistence may be present in a limited domain of parameter space.

Community dynamics for the first experiment, with possible extinctions, are shown by
Figure 6. Note that panel 1 represents the original simulation with ri = 1 ∀i, while ri
randomly varies between species for all other panels.

Figure 6. Visualisation of eight different simulations of twelve species on five resources. It is identical to Figure 4 except that intrinsic growth rates ri are randomly varied. Except for the first panel
(original Figure 4), the simulations chosen were randomly picked among the 500 constituting the


We observe contrasted stationary endpoints, possibly with some oscillations or chaos
during the invasion process. As shown in Figure 6, however, most species do not persist. For the second experiment, introducing all species at once, the percentage of experiments with x species present at different times of the simulation is displayed in Figure
7.


0204060020406005010005k10k020406005k10k05k10k05k10kTime (days)Time (days)Time (days)Time (days)AbundancesAbundancesAbundancesAbundances1 a)b)25 a)b)353 a)b)237 a)b)290 a)b)429 a)b)459 a)b)174 a)b)

Figure 7. Percentage of simulations with x species present, or with observable supersaturated coexistence, at different times of the simulation for the second experiment. 500 simulations have
been run in total and a species has been considered present if Ni > 0.001.

As before, a species has been considered present if Ni > 0.001 at the end of the simulation. The second experiment shows that persistence of five species or more is very unlikely when introducing all species at once (even more so than when introducing species
sequentially), and that supersaturated coexistence is consequently very rare in this configuration.

Community dynamics for the second experiment, with possible extinctions, are described
in the following Figure 8. Note that the subfigure 1 represents the original results with
ri = 1 ∀i, while ri randomly varies as described in the methods for all other panels.


0 species1 species2 species3 species4 species5 species6 species7 species8 species9 species10 species11 species12 speciesSupersaturated01020304050After 1000 daysAfter 3000 daysAfter 5000 daysAfter 10000 daysPercentage of simulations

Figure 8. Visualisation of eight different simulations of twelve species on five resources, following
the Figure 4 method except that ri was randomly drawn for each of the species and all species
were introduced at once. Except for the first panel (original parameters), the simulations illustrated were randomly picked among the 500 of the numerical experiment. Each couple of subplots is labelled with the number of the corresponding simulation. a) abundances of species 1‐6,
b) abundances of species 7‐12.

As for the first experiment, we mostly observed either fixed (non‐oscillatory) stationary
endpoints or oscillations (Figure 8), but with even less persistent species than for the
first experiment.

## 4 Discussion

We were able to successfully replicate the figures of the original paper. There are only
minor differences in species dynamics in Figure 4, which are arguably due to differences in numerical integration.

However, the additional numerical experiments showed that slightly changing the values of the ri parameters within a realistic range of values [10] almost always prevents
the coexistence of twelve species on five resources and mostly prevents supersaturated
coexistence in general. This is true when introducing species sequentially as in the original paper, as well as all at once.

Our results corroborate those of Schippers et al. [6], who showed that supersaturated
coexistence through chaos or oscillations requires particular sets of parameter values,
which are not robust to small perturbations. Our results, using a slightly different kind
of perturbation, are therefore consistent with their conclusion that supersaturated coexistence is unlikely to solve the paradox of the plankton. Additionally, there are other
reasons (mixing, spatial structure) not considered here, which could render supersaturated coexistence unlikely [11].


050100010203040024605k10k0204005k10k05k10k05k10kTime (days)Time (days)Time (days)Time (days)AbundancesAbundancesAbundancesAbundances1 a)b)343 a)b)271 a)b)128 a)b)461 a)b)418 a)b)161 a)b)35 a)b)

## 5 Appendix

We present below additional time series for random parameter sets and for the two numerical experiments. This is meant to help the reader to gain a better view of the dynamical behaviors for these two numerical experiments. The legends are identical to
those of Figures 6 and 8.

Figure 9. Visualisation of eight other different simulations of twelve species on five resources. It is
identical to Figure 4 except that intrinsic growth rates ri are randomly varied, and complements
Figure 6. The simulations chosen were randomly picked among the 500 constituting the first


050100020406002040608005k10k0204005k10k05k10k05k10kTime (days)Time (days)Time (days)Time (days)AbundancesAbundancesAbundancesAbundances360 a)b)59 a)b)146 a)b)428 a)b)201 a)b)420 a)b)373 a)b)73 a)b)

Figure 10. Visualisation of eight other different simulations of twelve species on five resources. It is
identical to Figure 4 except that intrinsic growth rates ri are randomly varied, and complements
Figure 6. The simulations chosen were randomly picked among the 500 constituting the first


020406080020406002040608005k10k020406005k10k05k10k05k10kTime (days)Time (days)Time (days)Time (days)AbundancesAbundancesAbundancesAbundances59 a)b)428 a)b)420 a)b)73 a)b)11 a)b)54 a)b)110 a)b)252 a)b)

Figure 11. Visualisation of eight other different simulations of twelve species on five resources. It is
identical to Figure 4 except that intrinsic growth rates ri are randomly varied, and complements
Figure 6. The simulations chosen were randomly picked among the 500 constituting the first


0204060020406005010005k10k020406005k10k05k10k05k10kTime (days)Time (days)Time (days)Time (days)AbundancesAbundancesAbundancesAbundances146 a)b)420 a)b)414 a)b)54 a)b)122 a)b)254 a)b)165 a)b)235 a)b)

Figure 12. Visualisation of eight other different simulations of twelve species on five resources,
following Figure 4, except that ri are randomly drawn for each of the species, and all species were
introduced at once (complements Figure 8). The simulations shown were randomly picked among
the 500 of the numerical experiment. Each couple of subplots is labelled with the number of the
corresponding simulation. a) abundances of species 1‐6, b) abundances of species 7‐12.


0510150102030400505k10k0204005k10k05k10k05k10kTime (days)Time (days)Time (days)Time (days)AbundancesAbundancesAbundancesAbundances471 a)b)174 a)b)358 a)b)224 a)b)70 a)b)47 a)b)167 a)b)371 a)b)

Figure 13. Visualisation of eight other different simulations of twelve species on five resources,
following Figure 4, except that ri are randomly drawn for each of the species, and all species were
introduced at once (complements Figure 8). The simulations shown were randomly picked among
the 500 of the numerical experiment. Each couple of subplots is labelled with the number of the
corresponding simulation. a) abundances of species 1‐6, b) abundances of species 7‐12.


02468020400246805k10k01020304005k10k05k10k05k10kTime (days)Time (days)Time (days)Time (days)AbundancesAbundancesAbundancesAbundances174 a)b)224 a)b)47 a)b)371 a)b)478 a)b)166 a)b)288 a)b)486 a)b)

Figure 14. Visualisation of eight other different simulations of twelve species on five resources,
following Figure 4, except that ri are randomly drawn for each of the species, and all species were
introduced at once (complements Figure 8). The simulations shown were randomly picked among
the 500 of the numerical experiment. Each couple of subplots is labelled with the number of the
corresponding simulation. a) abundances of species 1‐6, b) abundances of species 7‐12.

References

1.

J. Huisman and F. Weissing. “Biodiversity of plankton by species oscillations and chaos.” In: Nature 402 (1999),
pp. 309–309. DOI: https://doi.org/10.1038/46540.

2. G. Hutchinson.

“The Paradox of

the Plankton.”

In: The American Naturalist 95.882 (1961). DOI:

https://doi.org/10.1086/282171.

3. G. Hardin. “The Competitive Exclusion Principle.” In: Science 131.3409 (1960), pp. 1292–1297. DOI:

4.

5.

6.

7.

8.

9.

10.

https://doi.org/10.1126/science.131.3409.1292.
O. M. Phillips. “The Equilibrium and Stability of Simple Marine Biological Systems. I. Primary Nutrient Con-
sumers.” In: The American Naturalist 107.953 (1973). DOI: https://doi.org/10.1086/283553.
R. A. Armstrong and R. McGehee. “Competitive Exclusion.” In: The American Naturalist 115.2 (1980). DOI:
https://doi.org/10.1086/282818.
P. Schippers, A. M. Verschoor, M. Vos, and W. M. Mooij. “Does “supersaturated coexistence” resolve the
“paradox of the plankton”?” In: Ecology Letters 4.6 (2001), pp. 404–407. DOI: https://doi.org/10.1046/j.1461-
0248.2001.00239.x.
J. Huisman, A. M. Johansson, E. O. Folmer, and F. J. Weissing. “Towards a solution of the plankton para-
dox: the importance of physiology and life history.” In: Ecology Letters 4.5 (2001), pp. 408–411. DOI:
https://doi.org/10.1046/j.1461-0248.2001.00256.x.
Karline Soetaert, Thomas Petzoldt, and R. Woodrow Setzer. “Solving Differential Equations in R: Package deS-
olve.” In: Journal of Statistical Software 33.9 (2010), pp. 1–25. DOI: 10.18637/jss.v033.i09.
R Core Team. R: A Language and Environment for Statistical Computing. R Foundation for Statistical Com-
puting. Vienna, Austria, 2023. URL: https://www.R-project.org/.
E. L. Kyle F. Edwards Christopher A. Klausmeier. “Nutrient utilization traits of phytoplankton.” In: Ecology 96.8
(2015), pp. 2311–2311. DOI: https://doi.org/10.1890/14-2252.1.


02468020400102005k10k0204005k10k05k10k05k10kTime (days)Time (days)Time (days)Time (days)AbundancesAbundancesAbundancesAbundances358 a)b)47 a)b)214 a)b)166 a)b)487 a)b)162 a)b)440 a)b)445 a)b)

11.

D. L. Roelke and P. M. Eldridge. “Mixing of supersaturated assemblages and the precipitous loss of species.”
In: The American Naturalist 171.2 (2008), pp. 162–175. DOI: https://doi.org/10.1086/524955.

---
**Source PDF:** `518bcb3090ca.pdf` (2023_01_article.pdf)  
**URL:** https://zenodo.org/record/10371655/files/article.pdf
