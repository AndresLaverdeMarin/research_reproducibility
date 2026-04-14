R E S C I E N C E C

Reproduction / Earth sciences
[Re] Drivers of evapotranspiration from boreal wildfires

Ben Bond-Lamberty1, ID
1Joint Global Change Research Institute, Pacific Northwest National Laboratory, College Park, MD, USA

Edited by
Karthik Ram ID

Reviewed by
Jaclyn Hatala Matthes ID

Received
04 May 2020

Published
18 March 2021

Computational reproducibility is a difficult challenge across science. I attempted to use
R 3.6.1 to reproduce linear model fits, done originally using v2.6.0 for a 2009 paper on
the drivers of large‐scale forest evapotranspiration after wildfire. Model outputs were
largely identical, aside from minor formatting changes, except for one–out of 12 total–
regression in which the median residual value changed very slightly (in the sixth decimal
place). I suggest that this essentially successful reproducibility is due to the relative
simplicity of the script, its use of only base R functions, and R’s historically conservative
approach to breaking changes.

DOI
10.5281/zenodo.4617894

## 1 Introduction

Significant changes in forest fires have occurred in recent decades in the global boreal
(high latitude) forest, but the effects of changing climate and disturbance on evapotranspiration (ET) and forest water cycling more generally are not well understood. In a
previous study [1] we had explored the ecological and carbon‐cycle consequences of
changes in the fire regime using an ecosystem model run at high resolution across a
large (1000 km x 1000 km) area of the central Canadian boreal forest. In a subsequent
paper [2], we used the same model outputs to examine the hydrological implications of
these wildfire regime shifts [3].

How reproducible are the results reported in Bond‐Lamberty et al. 2009? The article
manuscript was written in 2007‐2008, initially submitted in April 2008, and a final, revised version was submitted in October of that year. The system timestamp on the script
output file is 2008‐03‐16. The methods section reports that R 2.6.0 [4], which was released
on 2007‐10‐03, was used for all analyses. The source code was not publicly archived, but
retained in the lead author’s personal records; it has no license. The original hardware
would have been an Apple laptop (probably a 2006‐2007 MacBook Pro). As noted above,
the code file was archived by the lead author, and so was easy for him (but no one else)
to find. The code has no comments or instructions.

## 2 Methods

### 2.1 Retrieval of the software

The source code being reproduced here is short and was written to analyze relationships between various potential driving factors and three output variables of interest:


Code is available at https://github.com/bpbond/ten-years-paper33. – SWH swh:1:rev:b8fe7506c23641ff7bc43deed4573feaa6d03947.
Data is available at https://github.com/bpbond/ten-years-paper33/blob/master/ET.csv.
Open peer review is available at https://github.com/ReScience/submissions/issues/40.


[Re] Drivers of evapotranspiration from boreal wildfires

ET, canopy evaporation, and canopy transpiration, all annual flux totals over the 19482005 model run period. The code simply reads in a comma‐separated data file holding
the modeling outputs, prints a summary of the data, and then fits and prints 12 separate
regressions (three output variables times four possible independent variables). These
fit statistics were reported on p. 1247 of Bond‐Lamberty et al. 2009.

### 2.2 Execution

Because the code uses only base R functions, it has no dependencies other than a standard R installation. Both in 2007‐2008 and 2020, the default Mac R installer provided
by CRAN was used to install R (i.e.
it was not built from source). The code was rerun, without modification, on a 2018 MacBook Pro under R version 3.6.1 (2019‐07‐05)
[5]; platform: x86\_64-apple-darwin15.6.0 (64‐bit); running under macOS Mojave 10.14.6. Its output was then compared with the printed output from the 2007‐2008
R 2.6.0 code, which had been recorded via R’s sink() function and archived with the
code.

## 3 Results and discussion

Setting aside minor spacing and text capitalization changes, only one numerical change
occurred, albeit in the sixth decimal place. In the 2008 R 2.6.0 output of a linear regression between canopy evaporation (dependent variable) and precipitation (independent),
the residuals were given as:

Residuals:

Median
-0.028858 -0.009186 0.002088

Min

1Q

3Q
0.010753

Max
0.019997

In the 2020 R 3.6.0 output, this output line (specifically, the ”Median” value) was:

Residuals:

Median
-0.028858 -0.009186 0.002089

Min

1Q

3Q
0.010753

Max
0.019997

In addition, in two cases p‐values were reported with a different number of significant
digits in the 2020 output: once gaining a digit (”0.005451” in 2020 versus ”0.00545” in
2008) and once losing one (”0.000103” and 0.0001030” respectively). No other numerical
differences occurred.

Whether these minor differences were due to the different R version, or different underlying operating system and/or libraries, is uncertain. R version 2.6.0 (https://cran.r-project.
org/bin/macosx/old/R-2.6.0.dmg) is unfortunately not installable under modern versions of
macOS. Instead I downloaded R 2.6.0 for Windows (i386-pc-mingw32) and ran the
code on it; the printed results were identical to the 2007‐2008 output file. This suggests
that the minor differences noted above between the R 2.6.0 and 3.6.0 outputs were due
to changes in R itself, not differences in the underlying systems.

As simple as the code and this reproducibility exercise was, there are some interesting
notes that can be drawn from it. Reproducibility has been a well‐supported (see e.g.
https://cran.r-project.org/web/views/ReproducibleResearch.html) core value of the R Core Team
and larger communnity, and the base version of the software has been highly stable over
the last twenty years since version 1.0. Specifically with regard to this exercise, the core
of the ‘lm‘ (linear model) source code, found at https://svn.r-project.org/R/trunk/src/library/
stats/R/lm.R, has changed little over the last decade. Refinements and extensions to R’s
linear modeling capabilities have instead come from contributed packages [6].


[Re] Drivers of evapotranspiration from boreal wildfires

In contrast, many of the most highly used R packages, for example those of the popular
tidyverse ecosystem [7] have historically changed their behavior and syntax much more
frequently. This allows for faster evolution and cleaner, consistent syntax (not among
base R’s strong points) but poses greater challenges for stable and reproducible software.
For example, the popular dplyr package lists (see https://github.com/tidyverse/dplyr/blob/
master/NEWS.md) breaking changes introduced at versions 0.5, 0.7, 0.7.5, 0.8, 0.8.1, and
1.0, over a timespan of four years; it seems unlikely that code taking advantage of its
powerful features and speed would be reproducible without being tweaked or rewritten.
This highlights some of the challenges surrounding computational reproducibility [8, 9],
in particular balancing reproducibility with other potentially important criteria such as
performance or confidentiality [10, 11].

## 4 Conclusions

There were many potential limitations in reproducing even this very short analysis script
over ten years later: the code contained no documentation about R or package versions,
nor information about the hardware information it was originally run on. The analysis
date could only be reconstructed from the output file timestamp (luckily unaltered). Saving this output file, however, at least allowed for a robust check on the reproducibility of
the analysis, script, and underlying R software after 12 years. The essentially successful
result is due to the relative simplicity of the script, its use of only base R functions, and
R’s conservative approach to breaking changes.

References

1.

2.

3.

4.

5.

6.

B. Bond-Lamberty, S. D. Peckham, D. E. Ahl, and S. T. Gower. “Fire as the dominant driver of central Canadian
boreal forest carbon balance.” en. In: Nature 450.7166 (Nov. 2007), pp. 89–92.
B. Bond-Lamberty, S. D. Peckham, S. T. Gower, and B. E. Ewers. “Effects of fire on regional evapotranspiration
in the central Canadian boreal forest.” In: Glob. Chang. Biol. 15.5 (2009), pp. 1242–1254.
R. H. Nolan, P. N. J. Lane, R. G. Benyon, R. A. Bradstock, and P. J. Mitchell. “Changes in evapotranspiration
following wildfire in resprouting eucalypt forests.” In: Ecohydrol. 6 (Jan. 2014).
R Core Team. R: A Language and Environment for Statistical Computing, Version 2.6.0. Vienna, Austria,
2007.
R Core Team. R: A Language and Environment for Statistical Computing, Version 3.6.1. Vienna, Austria,
2019.
U. Grömping. “Relative importance for linear regression in R: the package relaimpo.” In: J. Stat. Softw. 17.1
(2006), pp. 1–27.

7. H. Wickham, M. Averick, J. Bryan, W. Chang, L. McGowan, R. François, G. Grolemund, A. Hayes, L. Henry, J.

Hester, et al. “Welcome to the Tidyverse.” In: Journal of Open Source Software 4.43 (2019), p. 1686.
P. E. Thornton, R. B. Cook, B. H. Braswell, B. E. Law, W. M. Post, H. H. Shugart, B. T. Rhyne, and L. A. Hook.
“Archiving numerical models of biogeochemical dynamics.” In: EOS 86.44 (Nov. 2005), pp. 431–432.
J. S. S. Lowndes, B. D. Best, C. Scarborough, J. C. Afflerbach, M. R. Frazier, C. C. O’Hara, N. Jiang, and B. S.
Halpern. “Our path to better science in less time using open data science tools.” en. In: Nat Ecol Evol 1.6 (May
2017), p. 160.
V. Stodden. “Enabling reproducibility in big data research: Balancing confidentiality and scientific trans-
parency.” In: Privacy, Big Data, and the Public Good: Frameworks for Engagement 1 (2014), pp. 112–135.
R. D. Peng. “Reproducible research in computational science.” In: Science 334.6060 (2011), pp. 1226–1227.

8.

9.

10.

11.

---
**Source PDF:** `2020_21_article.pdf`
