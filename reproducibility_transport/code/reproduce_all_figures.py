###############################################################################
### Reproduce All Figures from:
### "Revisiting reproducibility in transportation simulation studies"
### Riehl, Kouvelas & Makridis (2025), European Transport Research Review
###############################################################################

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib.ticker import MaxNLocator

FIGURES_DIR = "../figures"

###############################################################################
# Load Data
###############################################################################
df_articleinfos = pd.read_excel("../data/ArticleInformation/ArticleInfos.xlsx")
survey_data_path = "../data/Survey/Simulation_Reproducibility_in_Transportation_Science_Submissions.csv"
df_survey = pd.read_csv(survey_data_path)
df_journal_infos = pd.read_excel("../data/JournalIndex_Top20/Journals_Top20.xlsx")
df_journal_infos = df_journal_infos.dropna()
df_journal_infos["journal"] = "journal_" + df_journal_infos["Nr"].astype(int).astype(str)

df_jif_infos = pd.read_excel("../data/ClarivateJournalCitationReports/JIF_History.xlsx")
del df_jif_infos["Journal"]
df_jif_infos = df_jif_infos.melt(id_vars=['Nr'], var_name='year', value_name='value')
df_jif_infos['year'] = df_jif_infos['year'].astype(int)
df_jif_infos = df_jif_infos.sort_values(['Nr', 'year']).reset_index(drop=True)
df_jif_infos = df_jif_infos.dropna()

###############################################################################
# Constants
###############################################################################
simulation_threshold = 5
year_threshold = 2014
year_col = "article_year"
simu_col = 'wc_simulation'

df_articleinfos_valid = df_articleinfos.copy()
df_articleinfos_valid = df_articleinfos_valid[df_articleinfos_valid[year_col].notna()]

journals = ["journal_2", "journal_3", "journal_4", "journal_5", "journal_6",
            "journal_7", "journal_8", "journal_9", "journal_10", "journal_11",
            "journal_13", "journal_14", "journal_15", "journal_17", "journal_18"]

journal_names = {
    "journal_2": "Transportation Research \n Part C",
    "journal_3": "Transportation Research \n Part D",
    "journal_4": "Transportation Research \n Part A",
    "journal_5": "Transportation Research \n Part E",
    "journal_6": "Transportation Research \n Part E",
    "journal_7": "Transport Policy",
    "journal_8": "Transportation Research \n Part B",
    "journal_9": "Journal of \n Transport Geography",
    "journal_10": "Transportation Research \n Part F",
    "journal_11": "Transportation Research \n Interdisciplinary Perspectives",
    "journal_13": "Computer-Aided Civil and \n Infrastructure Engineering",
    "journal_14": "Journal of Air \n Transport Management",
    "journal_15": "Transportation \n Research Procedia",
    "journal_17": "Transport Reviews",
    "journal_18": "International Journal \n of Pavement Engineering"
}

all_years = pd.DataFrame({year_col: range(2000, 2024)})


###############################################################################
# FIGURE 1: Simulation studies & repository availability over time
###############################################################################
print("Generating Figure 1...")

df_articles_per_year = df_articleinfos_valid.groupby(year_col).size().reset_index(name='count')
df_articles_per_year = all_years.merge(df_articles_per_year, on=year_col, how='left')
df_articles_per_year['count'] = df_articles_per_year['count'].fillna(0).astype(int)

df_simulation_studies_per_year = df_articleinfos_valid[df_articleinfos_valid[simu_col] >= simulation_threshold].groupby(year_col).size().reset_index(name="count")
df_simulation_studies_per_year = all_years.merge(df_simulation_studies_per_year, on=year_col, how='left')
df_simulation_studies_per_year['count'] = df_simulation_studies_per_year['count'].fillna(0).astype(int)

mask = (df_articleinfos_valid[simu_col] >= simulation_threshold) & (df_articleinfos_valid["has_repository"] == True)
df_filtered = df_articleinfos_valid[mask]
df_repo_studies_per_year = df_filtered.groupby(year_col).size().reset_index(name="count")
df_repo_studies_per_year = all_years.merge(df_repo_studies_per_year, on=year_col, how='left')
df_repo_studies_per_year['count'] = df_repo_studies_per_year['count'].fillna(0).astype(int)

mask = (df_articleinfos_valid[simu_col] >= simulation_threshold) & (df_articleinfos_valid["has_valid_repository"] == True)
df_filtered = df_articleinfos_valid[mask]
df_vrepo_studies_per_year = df_filtered.groupby(year_col).size().reset_index(name="count")
df_vrepo_studies_per_year = all_years.merge(df_vrepo_studies_per_year, on=year_col, how='left')
df_vrepo_studies_per_year['count'] = df_vrepo_studies_per_year['count'].fillna(0).astype(int)

plt.figure(figsize=(10, 3))

plt.subplot(1, 3, 1)
plt.title("Number of Studies")
plt.plot(df_articles_per_year[year_col], df_articles_per_year["count"], label="All Studies", color="black")
plt.plot(df_simulation_studies_per_year[year_col], df_simulation_studies_per_year["count"], label="Simulation Studies", color="gray")
plt.plot(df_vrepo_studies_per_year[year_col], df_vrepo_studies_per_year["count"], ":", label="with repository", color="gray")
plt.xlabel("Years")
plt.ylabel("Number of Articles")
plt.legend()

plt.subplot(1, 3, 2)
plt.title("Share of Simulation Studies")
plt.plot(df_simulation_studies_per_year[year_col], df_simulation_studies_per_year["count"] / df_articles_per_year["count"] * 100, color="black")
plt.xlabel("Years")
plt.ylabel("Share of All Articles [%]")

plt.subplot(1, 3, 3)
plt.title("(with Repository)\nShare of Simulation Studies")
plt.plot(df_simulation_studies_per_year[year_col], df_vrepo_studies_per_year["count"] / df_simulation_studies_per_year["count"] * 100, color="black")
plt.xlabel("Years")
plt.ylabel("Share of Simulation Articles [%]")

plt.tight_layout()
plt.subplots_adjust(top=0.84, bottom=0.165)
plt.savefig(f"{FIGURES_DIR}/Figure_1_simulation_studies_availability.png", dpi=300, bbox_inches='tight')
plt.close()
print("  -> Figure 1 saved.")


###############################################################################
# FIGURE 2: Repositories & journal impact
###############################################################################
print("Generating Figure 2...")

# Prepare data for Analysis 4
df_articleinfos_valid_l5y = df_articleinfos_valid[df_articleinfos_valid[year_col] >= year_threshold]
df_articles_per_journal = df_articleinfos_valid_l5y.groupby('journal').size().reset_index(name='count')
df_simulation_studies_per_journal = df_articleinfos_valid_l5y[df_articleinfos_valid_l5y[simu_col] >= simulation_threshold].groupby("journal").size().reset_index(name="count")

mask = (df_articleinfos_valid_l5y[simu_col] >= simulation_threshold) & (df_articleinfos_valid_l5y["has_valid_repository"] == True)
df_vrepo_studies_per_journal = df_articleinfos_valid_l5y[mask].groupby("journal").size().reset_index(name="count")

df_articleinfos_valid_l5y2 = df_articleinfos_valid[df_articleinfos_valid[year_col] >= year_threshold]
df_articleinfos_valid_l5y2 = df_articleinfos_valid_l5y2[df_articleinfos_valid_l5y2[simu_col] >= simulation_threshold]
df_articleinfos_valid_l5y2['repo_score'] = df_articleinfos_valid_l5y2['repo_score'].fillna(0)
df_articleinfos_valid_l5y2 = df_articleinfos_valid_l5y2.merge(df_jif_infos, left_on=["journal", "article_year"], right_on=["Nr", "year"], how="left")
df_articleinfos_valid_l5y2["has_repo"] = df_articleinfos_valid_l5y2["repo_score"] > 0
df_articleinfos_valid_l5y2['has_repo'] = df_articleinfos_valid_l5y2['has_repo'].astype(int)

df_articleinfos_valid_l5y3 = df_articleinfos_valid_l5y2[df_articleinfos_valid_l5y2["repo_score"] > 0]

df_journals_data = df_journal_infos[["journal", "h5-index", "h5-median"]]
df_scatter_journal_data = df_articles_per_journal.copy()
df_scatter_journal_data = df_scatter_journal_data.merge(df_vrepo_studies_per_journal, on="journal", how="left")
df_scatter_journal_data = df_scatter_journal_data.merge(df_journals_data, on="journal", how="left")
df_scatter_journal_data = df_scatter_journal_data.merge(df_simulation_studies_per_journal, on="journal", how="left")
df_scatter_journal_data = df_scatter_journal_data.rename(columns={
    "count_x": "n_articles",
    "count_y": "n_repo",
    "count": "n_simstud"
})

plt.figure(figsize=(10, 3))

plt.subplot(1, 3, 1)
plt.scatter(df_scatter_journal_data["h5-median"], df_scatter_journal_data["n_repo"] / df_scatter_journal_data["n_simstud"] * 100, color="black")
plt.xlabel("Journal Impact (h5-median)")
plt.ylabel("with Repository [%]")

df_scatter_journal_data2 = df_scatter_journal_data.dropna()
df_scatter_journal_data2 = df_scatter_journal_data2.sort_values(by="h5-median", ascending=True)
x = df_scatter_journal_data2["h5-median"]
y = df_scatter_journal_data2["n_repo"] / df_scatter_journal_data2["n_simstud"] * 100
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), "--", color="gray")

plt.subplot(1, 3, 2)
df_articleinfos_valid_l5y2['value_bins'] = pd.cut(df_articleinfos_valid_l5y2['value'], bins=10)
numeric_columns = df_articleinfos_valid_l5y2.select_dtypes(include=[np.number]).columns
numeric_columns = numeric_columns.drop(['value'])
result = df_articleinfos_valid_l5y2.groupby('value_bins')[numeric_columns].mean().reset_index()
result['value_bins_str'] = result['value_bins'].apply(lambda x: f"{x.mid:.2f}")

plt.bar(result["value_bins_str"], np.asarray(result["has_repo"]) * 100)
plt.xlabel('Journal Impact Factor (Crossref)')
plt.ylabel('with Repository [%]')

num_ticks = 5
step = max(1, len(result) // (num_ticks - 1))
tick_locations = range(0, len(result), step)
tick_labels = [result["value_bins_str"].iloc[i] for i in tick_locations]
plt.xticks(list(tick_locations), tick_labels, ha='right')

plt.subplot(1, 3, 3)
sns.violinplot(y='repo_score', x='value', orient='h', data=df_articleinfos_valid_l5y2, color='C0')
plt.xlabel('Journal Impact Factor (Crossref)')
plt.ylabel('Repository Score')
plt.yticks(range(6), ['0', '1', '2', '3', '4', '5'])

plt.tight_layout()
plt.subplots_adjust(top=0.95, bottom=0.164, wspace=0.256)
plt.savefig(f"{FIGURES_DIR}/Figure_2_repositories_journal_impact.png", dpi=300, bbox_inches='tight')
plt.close()
print("  -> Figure 2 saved.")


###############################################################################
# FIGURE 3: Repositories over time
###############################################################################
print("Generating Figure 3...")

year_threshold_detail = 2017

mask = (df_articleinfos_valid[simu_col] >= simulation_threshold) & (df_articleinfos_valid["has_valid_repository"] == True)
df_filtered = df_articleinfos_valid[mask]
df_vrepo_studies_per_year2 = df_filtered.groupby(year_col).size().reset_index(name="count")
df_vrepo_studies_per_year2 = all_years.merge(df_vrepo_studies_per_year2, on=year_col, how='left')
df_vrepo_studies_per_year2['count'] = df_vrepo_studies_per_year2['count'].fillna(0).astype(int)

df_repo_infos = df_articleinfos_valid.copy()
df_repo_infos = df_repo_infos[df_repo_infos[simu_col] >= simulation_threshold]
df_repo_infos = df_repo_infos[df_repo_infos["has_valid_repository"] == True]
df_repo_infos["rep_score_1"] = df_repo_infos["repo_score"] == 1
df_repo_infos["rep_score_2"] = df_repo_infos["repo_score"] == 2
df_repo_infos["rep_score_3"] = df_repo_infos["repo_score"] == 3
df_repo_infos["rep_score_4"] = df_repo_infos["repo_score"] == 4
df_repo_infos["rep_score_5"] = df_repo_infos["repo_score"] == 5
df_repo_infos = df_repo_infos[["journal", year_col, 'has_video',
                                'has_code', 'has_dataset',
                                'has_model', 'has_documentation',
                                'has_license', 'repo_score',
                                'rep_score_1', "rep_score_2", "rep_score_3", "rep_score_4", "rep_score_5"]]

article_stats = df_repo_infos.groupby(year_col).agg({
    'has_video': ['sum'], "has_code": ["sum"], "has_dataset": ["sum"],
    "has_model": ["sum"], "has_documentation": ["sum"], "has_license": ["sum"], "repo_score": ["mean"],
    "rep_score_1": ["sum"], "rep_score_2": ["sum"], "rep_score_3": ["sum"], "rep_score_4": ["sum"], "rep_score_5": ["sum"],
}).reset_index()
article_stats.columns = [year_col, 'n_video', 'n_code', 'n_dataset', 'n_model', 'n_documentation',
                         'n_license', "av_reposcore", "n_repo1", "n_repo2", "n_repo3", "n_repo4", "n_repo5"]

df_reprod_time = df_vrepo_studies_per_year2.copy()
df_reprod_time = df_reprod_time.merge(article_stats, on=year_col, how="left")
df_reprod_time = df_reprod_time[df_reprod_time[year_col] >= year_threshold_detail]

plt.figure(figsize=(10, 3))

plt.subplot(1, 3, 1)
plt.plot(df_reprod_time[year_col], df_reprod_time["n_video"] / df_reprod_time["count"] * 100, label="has video")
plt.plot(df_reprod_time[year_col], df_reprod_time["n_code"] / df_reprod_time["count"] * 100, label="has code")
plt.plot(df_reprod_time[year_col], df_reprod_time["n_dataset"] / df_reprod_time["count"] * 100, label="has data")
plt.plot(df_reprod_time[year_col], df_reprod_time["n_model"] / df_reprod_time["count"] * 100, label="has model")
plt.plot(df_reprod_time[year_col], df_reprod_time["n_documentation"] / df_reprod_time["count"] * 100, label="has documentation")
plt.plot(df_reprod_time[year_col], df_reprod_time["n_license"] / df_reprod_time["count"] * 100, label="has license")
plt.xlabel("Year")
plt.ylabel("Repository With ... [%]")
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.3), ncol=3, fontsize='x-small')
plt.ylim(0, 100)

plt.subplot(1, 3, 2)
plt.gca().stackplot(df_reprod_time['article_year'],
             df_reprod_time['n_repo1'] / df_reprod_time["count"] * 100,
             df_reprod_time['n_repo2'] / df_reprod_time["count"] * 100,
             df_reprod_time['n_repo3'] / df_reprod_time["count"] * 100,
             df_reprod_time['n_repo4'] / df_reprod_time["count"] * 100,
             df_reprod_time['n_repo5'] / df_reprod_time["count"] * 100,
             labels=['Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5'],
             colors=plt.cm.Greys(np.linspace(0.2, 0.8, 5)))
plt.xlabel("Year")
plt.ylabel("Repository With ... Score [%]")
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.3), ncol=3, fontsize='x-small')
plt.ylim(0, 100)

plt.subplot(1, 3, 3)
plt.plot(df_reprod_time[year_col], df_reprod_time["av_reposcore"], label="Average Level")
plt.xlabel("Year")
plt.ylabel("Avg. Repository Level")
plt.ylim(0, 5)

plt.tight_layout()
plt.savefig(f"{FIGURES_DIR}/Figure_3_repositories_over_time.png", dpi=300, bbox_inches='tight')
plt.close()
print("  -> Figure 3 saved.")


###############################################################################
# FIGURE 4: Survey demographics
###############################################################################
print("Generating Figure 4...")

def drawQuestionBarPlotDemo(df, question, value_space, xticklabels):
    value_counts = df[question].value_counts()
    counts = value_counts.reindex(value_space, fill_value=0)
    bars = plt.bar(counts.index, counts.values)
    plt.xticks(counts.index)
    for bar in bars:
        height = bar.get_height()
        text = f'{height}'
        if height > 2:
            plt.text(bar.get_x() + bar.get_width() / 2, height / 2, text,
                     ha='center', va='center', color="white")
        else:
            plt.text(bar.get_x() + bar.get_width() / 2, height, text,
                     ha='center', va='bottom')
    plt.gca().set_xticklabels(xticklabels, ha='right')
    plt.xticks(rotation=45)
    plt.yticks([], [])

fig = plt.figure(figsize=(10, 3))

plt.subplot(1, 3, 1)
plt.title('Research Experience', fontsize=10)
drawQuestionBarPlotDemo(df_survey,
                    question='1) Research Experience',
                    value_space=["1-2", "2-3", "3-4", "5-10", "10+"],
                    xticklabels=["1-2", "2-3", "3-4", "5-10", "10+"])

plt.subplot(1, 3, 2)
plt.title('Position', fontsize=10)
drawQuestionBarPlotDemo(df_survey,
                    question='2) Current Position',
                    value_space=["Master Student", "PhD / Doctoral Student", "Post-Doc", "Assistant / Junior Professor", "Tenure Track / Senior Professor"],
                    xticklabels=["Master Student", "PhD Student", "Post-Doc", "Junior Professor", "Senior Professor"])

plt.subplot(1, 3, 3)
plt.title('Region', fontsize=10)
drawQuestionBarPlotDemo(df_survey,
                    question='3) Where is your research organization located?',
                    value_space=["Africa", "Asia", "Australia & Oceania", "Europe", "Middle East", "North America", "South America"],
                    xticklabels=["Africa", "Asia", "Australia & Oceania", "Europe", "Middle East", "North America", "South America"])

plt.tight_layout()
plt.subplots_adjust(top=0.9, hspace=0.45)
plt.savefig(f"{FIGURES_DIR}/Figure_4_survey_demographics.png", dpi=300, bbox_inches='tight')
plt.close()
print("  -> Figure 4 saved.")


###############################################################################
# FIGURE 5: Survey perception by position & region
###############################################################################
print("Generating Figure 5...")

fig = plt.figure(figsize=(10, 3))

position_order = ["Master Student", "PhD / Doctoral Student", "Post-Doc", "Assistant / Junior Professor", "Tenure Track / Senior Professor"]
position = '2) Current Position'
yticklabels = ["Master Student", "PhD Student", "Post-Doc", "Junior Professor", "Senior Professor"]

plt.subplot(2, 4, 1)
plt.title('Reproducibility As\nSignificant Issue', fontsize=10)
vote = 'The lack of reproducibility in simulation studies is a significant issue in the transportation literature'
dfX = df_survey[[position, vote]]
dfX = dfX.groupby(position)[vote].agg(['mean', 'std']).reset_index()
dfX[position] = pd.Categorical(dfX[position], categories=position_order, ordered=True)
dfX = dfX.sort_values(position)
plt.barh(dfX[position], dfX['mean'], xerr=dfX['std'], capsize=5, error_kw={'ecolor': 'black', 'capthick': 2}, zorder=2)
plt.xlim(1, 5.5)
plt.grid(zorder=1, axis='x')
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.gca().set_yticklabels(yticklabels, ha='right')
prev_ax = plt.gca()

plt.subplot(2, 4, 2)
plt.title('Need For More Transparency\n(Data, Code, Models)', fontsize=10)
vote = 'There is a need for greater transparency from researchers regarding their code, data, and simulation models'
dfX = df_survey[[position, vote]]
dfX = dfX.groupby(position)[vote].agg(['mean', 'std']).reset_index()
dfX[position] = pd.Categorical(dfX[position], categories=position_order, ordered=True)
dfX = dfX.sort_values(position)
plt.barh(dfX[position], dfX['mean'], xerr=dfX['std'], capsize=5, error_kw={'ecolor': 'black', 'capthick': 2}, zorder=2)
plt.grid(zorder=1)
plt.yticks([], [])
plt.xlim(1, 5.5)
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))

plt.subplot(2, 4, 3)
plt.title('Mandatory Data\nAvailability Statement', fontsize=10)
vote = 'Journals should mandate data availability statements and repositories \nto ensure reproducibility (e.g. GitHub, BitBucket, SourceForge, Mendeley) '
dfX = df_survey[[position, vote]]
dfX = dfX.groupby(position)[vote].agg(['mean', 'std']).reset_index()
dfX[position] = pd.Categorical(dfX[position], categories=position_order, ordered=True)
dfX = dfX.sort_values(position)
plt.barh(dfX[position], dfX['mean'], xerr=dfX['std'], capsize=5, error_kw={'ecolor': 'black', 'capthick': 2}, zorder=2)
plt.xlim(1, 5.5)
plt.grid(zorder=1)
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.yticks([], [])

plt.subplot(2, 4, 4)
plt.title('Implemented Strategy\nIn Their Groups [%]', fontsize=10)
vote = 'Our research group has implemented some type of measure to enhance reproducibility in our work'
dfX = df_survey[[position, vote]]
dfX["agree"] = dfX[vote] == "Yes"
dfX = dfX.groupby(position)["agree"].agg(['sum', "count"]).reset_index()
dfX["agree"] = dfX["sum"] / dfX["count"]
dfX[position] = pd.Categorical(dfX[position], categories=position_order, ordered=True)
dfX = dfX.sort_values(position)
bars = plt.barh(dfX[position], dfX['agree'] * 100, capsize=5, error_kw={'ecolor': 'black', 'capthick': 2}, zorder=2)
for i, bar in enumerate(bars):
    width = bar.get_width()
    count = dfX['count'].iloc[i]
    plt.gca().text(width + 1, bar.get_y() + bar.get_height() / 2, f'n={count}',
            va='center', ha='left', fontsize=10)
plt.xlim(1, 100)
plt.grid(zorder=1)
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.yticks([], [])
plt.xticks([0, 25, 50, 75, 100])

# Bottom row: by region
position = '3) Where is your research organization located?'

plt.subplot(2, 4, 5)
vote = 'The lack of reproducibility in simulation studies is a significant issue in the transportation literature'
dfX = df_survey[[position, vote]]
dfX = dfX.groupby(position)[vote].agg(['mean', 'std']).reset_index()
dfX = dfX.sort_values(position)
plt.barh(dfX[position], dfX['mean'], xerr=dfX['std'], capsize=5, error_kw={'ecolor': 'black', 'capthick': 2}, zorder=2)
plt.xlim(1, 5.5)
plt.grid(zorder=1, axis='x')
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))

plt.subplot(2, 4, 6)
vote = 'There is a need for greater transparency from researchers regarding their code, data, and simulation models'
dfX = df_survey[[position, vote]]
dfX = dfX.groupby(position)[vote].agg(['mean', 'std']).reset_index()
dfX = dfX.sort_values(position)
plt.barh(dfX[position], dfX['mean'], xerr=dfX['std'], capsize=5, error_kw={'ecolor': 'black', 'capthick': 2}, zorder=2)
plt.grid(zorder=1)
plt.yticks([], [])
plt.xlim(1, 5.5)
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))

plt.subplot(2, 4, 7)
vote = 'Journals should mandate data availability statements and repositories \nto ensure reproducibility (e.g. GitHub, BitBucket, SourceForge, Mendeley) '
dfX = df_survey[[position, vote]]
dfX = dfX.groupby(position)[vote].agg(['mean', 'std']).reset_index()
dfX = dfX.sort_values(position)
plt.barh(dfX[position], dfX['mean'], xerr=dfX['std'], capsize=5, error_kw={'ecolor': 'black', 'capthick': 2}, zorder=2)
plt.xlim(1, 5.5)
plt.grid(zorder=1)
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.yticks([], [])

plt.subplot(2, 4, 8)
vote = 'Our research group has implemented some type of measure to enhance reproducibility in our work'
dfX = df_survey[[position, vote]]
dfX["agree"] = dfX[vote] == "Yes"
dfX = dfX.groupby(position)["agree"].agg(['sum', "count"]).reset_index()
dfX["agree"] = dfX["sum"] / dfX["count"]
dfX = dfX.sort_values(position)
bars = plt.barh(dfX[position], dfX['agree'] * 100, capsize=5, error_kw={'ecolor': 'black', 'capthick': 2}, zorder=2)
for i, bar in enumerate(bars):
    width = bar.get_width()
    count = dfX['count'].iloc[i]
    plt.gca().text(width + 1, bar.get_y() + bar.get_height() / 2, f'n={count}',
            va='center', ha='left', fontsize=10)
plt.xlim(1, 100)
plt.grid(zorder=1)
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.yticks([], [])
plt.xticks([0, 25, 50, 75, 100])

plt.tight_layout()
plt.savefig(f"{FIGURES_DIR}/Figure_5_survey_perception.png", dpi=300, bbox_inches='tight')
plt.close()
print("  -> Figure 5 saved.")


###############################################################################
# FIGURE 6: Survey questionnaire results (5x4 grid)
###############################################################################
print("Generating Figure 6...")

value_space = [1, 2, 3, 4, 5]

def drawQuestionBarPlot(df, question):
    value_counts = df[question].value_counts()
    average = np.mean(df[question])
    counts = value_counts.reindex(value_space, fill_value=0)
    bars = plt.bar(counts.index, counts.values)
    plt.xticks(counts.index)
    plt.text(0.05, 0.95, f'Avg: {average:.2f}',
             transform=plt.gca().transAxes,
             fontsize=10, fontweight='bold',
             verticalalignment='top',
             bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=2))
    for bar in bars:
        height = bar.get_height()
        text = f'{height}'
        if height > 2:
            plt.text(bar.get_x() + bar.get_width() / 2, height / 2, text,
                     ha='center', va='center', color="white")
        else:
            plt.text(bar.get_x() + bar.get_width() / 2, height, text,
                     ha='center', va='bottom')
    plt.axvline(x=average, color='black', linestyle='--', label=f'Average: {average:.2f}')
    plt.xticks([], [])
    plt.yticks([], [])

def drawQuestionBarPlotYesNo(df, question):
    n_yes = sum(df[question] == "Yes")
    n_no = sum(df[question] == "No")
    categories = ['Yes', 'No']
    values = [n_yes, n_no]
    bars = plt.bar(categories, values, color=['tab:blue', 'tab:blue'])
    plt.xticks(categories)
    ctr = 0
    for bar in bars:
        height = bar.get_height()
        if ctr == 0:
            average = n_yes / (n_yes + n_no) * 100
            plt.text(bar.get_x() + bar.get_width() / 2, height / 4,
                     f'Yes [{n_yes}]\n{average:.0f}%',
                     ha='center', va='bottom', color="white")
            ctr = 1
        else:
            average = n_no / (n_yes + n_no) * 100
            plt.text(bar.get_x() + bar.get_width() / 2, height / 2,
                     f'No [{n_no}]\n{average:.0f}%',
                     ha='center', va='bottom', color="white")
    plt.ylim(bottom=0)
    plt.xticks([], [])
    plt.yticks([], [])

def drawDoubleQuestionBarPlot(df, question1, question2):
    value_counts1 = df[question1].value_counts()
    value_counts2 = df[question2].value_counts()
    average1 = np.mean(df[question1])
    average2 = np.mean(df[question2])
    counts1 = value_counts1.reindex(value_space, fill_value=0)
    counts2 = value_counts2.reindex(value_space, fill_value=0)
    x = np.arange(len(value_space))
    width = 0.35
    bars1 = plt.bar(x - width / 2, counts1.values, width, color='tab:blue', label=f"Me [{average1:.2f}]")
    bars2 = plt.bar(x + width / 2, counts2.values, width, color='tab:green', label=f"Others [{average2:.2f}]")
    plt.xticks(x, value_space)
    def add_labels(bars):
        for bar in bars:
            height = bar.get_height()
            text = f'{height}'
            if height > 2:
                plt.text(bar.get_x() + bar.get_width() / 2, height / 2, text,
                         ha='center', va='center', color="white")
            else:
                plt.text(bar.get_x() + bar.get_width() / 2, height, text,
                         ha='center', va='bottom')
    add_labels(bars1)
    add_labels(bars2)
    plt.axvline(x=average1 - 1, color='black', linestyle='--')
    plt.axvline(x=average2 - 1, color='black', linestyle=':')
    plt.legend(fontsize='x-small', ncol=2, loc='upper right', bbox_to_anchor=(1, 1.02))
    plt.xticks([], [])
    plt.yticks([], [])

fig = plt.figure(figsize=(10, 7))

# Row 1: Perceived Severity (Q1.1-1.4)
plt.subplot(5, 4, 1)
plt.title('Q1.1: Reproducibility As\nSignificant Issue', fontsize=10)
drawQuestionBarPlot(df_survey, question="The lack of reproducibility in simulation studies is a significant issue in the transportation literature")

plt.subplot(5, 4, 2)
plt.title('Q1.2: Spent Unnecessary\nEfforts To Reproduce', fontsize=10)
drawQuestionBarPlot(df_survey, question="I have invested considerable time and effort in attempting to reproduce existing studies (which could have been avoided, e.g. with better documentation)")

plt.subplot(5, 4, 3)
plt.title('Q1.3: Need For More\nTransparency (Data, Code, Models)', fontsize=10)
drawQuestionBarPlot(df_survey, question="There is a need for greater transparency from researchers regarding their code, data, and simulation models")

plt.subplot(5, 4, 4)
plt.title('Q1.4: Mandatory Data\nAvailability Statement', fontsize=10)
drawQuestionBarPlot(df_survey, question="New publications should be required to include a basic online repository and data availability statement")

# Row 2-3: Factors Influencing Transparency (Q2.1-2.8)
plt.subplot(5, 4, 5)
plt.title('Q2.1: Legal Constraints', fontsize=10)
drawQuestionBarPlot(df_survey, question="I cannot publish due to legal constraints (e.g., data privacy, intellectual property rights)")

plt.subplot(5, 4, 6)
plt.title('Q2.2: Quality Concerns', fontsize=10)
drawQuestionBarPlot(df_survey, question="I have concerns about the quality of reliability of my simulations")

plt.subplot(5, 4, 7)
plt.title('Q2.3: Lack of Confidence', fontsize=10)
drawQuestionBarPlot(df_survey, question="I lack confidence and/or feel vulnerable in sharing code, data, or models publicly")

plt.subplot(5, 4, 8)
plt.title('Q2.4: Time Constraints', fontsize=10)
drawQuestionBarPlot(df_survey, question="I have time constraints (that limit efforts in preparing repositories and managing data-sharing agreements to the desired level)")

plt.subplot(5, 4, 9)
plt.title('Q2.5: Lack of Knowledge', fontsize=10)
drawQuestionBarPlot(df_survey, question='I lack knowledge about tools and best practices for managing repositories')

plt.subplot(5, 4, 10)
plt.title('Q2.6: Upon Request\nIs Sufficient', fontsize=10)
drawQuestionBarPlot(df_survey, question='I believe sharing data upon request is sufficient (e.g., via email)')

plt.subplot(5, 4, 11)
plt.title('Q2.7: Fear Reduced Chances\nOf Publication', fontsize=10)
drawDoubleQuestionBarPlot(df_survey, 'I fear transparency might hinder chances of publication acceptance',
                              'Other researchers fear transparency might hinder chances of publication acceptance')

plt.subplot(5, 4, 12)
plt.title('Q2.8: Intentionally To\nMaintain Advantage', fontsize=10)
drawDoubleQuestionBarPlot(df_survey, 'I intentionally withhold materials to maintain a competitive advantage',
                              'Other researchers intentionally withhold materials to maintain what they believe to be a competitive advantage')

# Row 4-5: Suggestions for Improvement (Q3.1-3.7)
plt.subplot(5, 4, 13)
plt.title('Q3.1: Publish Data', fontsize=10)
drawQuestionBarPlot(df_survey, question="Researchers should publish data (raw or processed)")

plt.subplot(5, 4, 14)
plt.title('Q3.2: Publish Models', fontsize=10)
drawQuestionBarPlot(df_survey, question="Researchers should publish simulation models")

plt.subplot(5, 4, 15)
plt.title('Q3.3: Publish Software Code', fontsize=10)
drawQuestionBarPlot(df_survey, question="Researchers should publish software / source code")

plt.subplot(5, 4, 16)
plt.title('Q3.4: Publish Online Appendix', fontsize=10)
drawQuestionBarPlot(df_survey, question="Researchers should publish a comprehensive online appendix alongside each study, detailing the methodologies")

plt.subplot(5, 4, 17)
plt.title('Q3.5: Data\nAvailability Statement', fontsize=10)
drawQuestionBarPlot(df_survey, question="Journals should mandate data availability statements and repositories \nto ensure reproducibility (e.g. GitHub, BitBucket, SourceForge, Mendeley) ")

plt.subplot(5, 4, 18)
plt.title('Q3.6: Funding Agencies\nShould Require Strategy', fontsize=10)
drawQuestionBarPlot(df_survey, question="Funding agencies should require detailed reproducibility plans in grant proposals")

plt.subplot(5, 4, 19)
plt.title('Q3.7: Research Group\nImplemented Strategy', fontsize=10)
drawQuestionBarPlotYesNo(df_survey, question="Our research group has implemented some type of measure to enhance reproducibility in our work")

plt.tight_layout()
plt.subplots_adjust(top=0.9, hspace=0.45)

# Add horizontal dividing lines
fig.add_subplot(111, frameon=False)
plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
plt.axhline(y=0.83, color='black', linestyle='-', linewidth=2.5)
plt.axhline(y=0.4, color='black', linestyle='-', linewidth=2.5)

plt.savefig(f"{FIGURES_DIR}/Figure_6_survey_questionnaire_results.png", dpi=300, bbox_inches='tight')
plt.close()
print("  -> Figure 6 saved.")


print("\nAll figures saved to:", FIGURES_DIR)


###############################################################################
# STATISTICAL VALIDATION (Section 2.3 of paper_summary.md)
###############################################################################
from scipy import stats

print("\n" + "=" * 70)
print("STATISTICAL VALIDATION - Reproducing Section 2.3 of paper_summary.md")
print("=" * 70)

# Paper-reported values
paper_values = {
    "sim_vs_nosim": {
        "t_test_p":        9.06e-45,
        "mannwhitney_p":   1.93e-110,
        "kruskalwallis_p": 3.87e-110,
        "mean_sim":        4.39,
        "mean_nosim":      3.55,
    },
    "repo_vs_norepo": {
        "t_test_p":        0.324,
        "mannwhitney_p":   0.218,
        "kruskalwallis_p": 0.437,
        "mean_with_repo":  4.56,
        "mean_no_repo":    4.39,
    },
}

# --- Prepare groups ---
df_reg = df_articleinfos_valid.copy()
cits_nosim = df_reg[df_reg[simu_col] < simulation_threshold]["num_cits_per_year"].dropna()
cits_sim   = df_reg[df_reg[simu_col] >= simulation_threshold]["num_cits_per_year"].dropna()

df_sim_only = df_reg[df_reg[simu_col] >= simulation_threshold]
cits_with_repo = df_sim_only[df_sim_only["has_repository"] == True]["num_cits_per_year"].dropna()
cits_no_repo   = df_sim_only[df_sim_only["has_repository"] == False]["num_cits_per_year"].dropna()

# =========================================================================
# Comparison 1: Non-Simulation vs. Simulation
# =========================================================================
print("\n--- Comparison 1: Non-Simulation vs. Simulation ---")

mean_sim = cits_sim.mean()
mean_nosim = cits_nosim.mean()
print(f"  Mean citations/year (Simulation):     {mean_sim:.2f}  (paper: {paper_values['sim_vs_nosim']['mean_sim']:.2f})")
print(f"  Mean citations/year (Non-Simulation): {mean_nosim:.2f}  (paper: {paper_values['sim_vs_nosim']['mean_nosim']:.2f})")

# T-test (one-sided: simulation > non-simulation)
t_stat, t_p = stats.ttest_ind(cits_sim, cits_nosim, alternative='greater')
print(f"\n  T-test:")
print(f"    T-statistic:  {t_stat:.3f}")
print(f"    p-value:      {t_p:.2e}   (paper: {paper_values['sim_vs_nosim']['t_test_p']:.2e})")
print(f"    Match:        {'YES' if abs(t_p - paper_values['sim_vs_nosim']['t_test_p']) / max(paper_values['sim_vs_nosim']['t_test_p'], 1e-300) < 0.1 else 'CLOSE' if abs(t_p - paper_values['sim_vs_nosim']['t_test_p']) / max(paper_values['sim_vs_nosim']['t_test_p'], 1e-300) < 1.0 else 'DIFFERS'}")

# Mann-Whitney U test (one-sided)
u_stat, mw_p = stats.mannwhitneyu(cits_sim, cits_nosim, alternative='greater')
print(f"\n  Mann-Whitney U test:")
print(f"    U-statistic:  {u_stat:,.1f}")
print(f"    p-value:      {mw_p:.2e}   (paper: {paper_values['sim_vs_nosim']['mannwhitney_p']:.2e})")
print(f"    Match:        {'YES' if mw_p == 0.0 and paper_values['sim_vs_nosim']['mannwhitney_p'] < 1e-100 else 'YES' if abs(mw_p - paper_values['sim_vs_nosim']['mannwhitney_p']) / max(paper_values['sim_vs_nosim']['mannwhitney_p'], 1e-300) < 0.1 else 'CLOSE' if abs(mw_p - paper_values['sim_vs_nosim']['mannwhitney_p']) / max(paper_values['sim_vs_nosim']['mannwhitney_p'], 1e-300) < 1.0 else 'DIFFERS'}")

# Kruskal-Wallis H test (two-sided)
h_stat, kw_p = stats.kruskal(cits_sim, cits_nosim)
print(f"\n  Kruskal-Wallis H test:")
print(f"    H-statistic:  {h_stat:.3f}")
print(f"    p-value:      {kw_p:.2e}   (paper: {paper_values['sim_vs_nosim']['kruskalwallis_p']:.2e})")
print(f"    Match:        {'YES' if kw_p == 0.0 and paper_values['sim_vs_nosim']['kruskalwallis_p'] < 1e-100 else 'YES' if abs(kw_p - paper_values['sim_vs_nosim']['kruskalwallis_p']) / max(paper_values['sim_vs_nosim']['kruskalwallis_p'], 1e-300) < 0.1 else 'CLOSE' if abs(kw_p - paper_values['sim_vs_nosim']['kruskalwallis_p']) / max(paper_values['sim_vs_nosim']['kruskalwallis_p'], 1e-300) < 1.0 else 'DIFFERS'}")

# =========================================================================
# Comparison 2: With Repository vs. Without Repository
# =========================================================================
print("\n--- Comparison 2: With Repository vs. Without Repository ---")

mean_with = cits_with_repo.mean()
mean_without = cits_no_repo.mean()
print(f"  Mean citations/year (With Repo):    {mean_with:.2f}  (paper: {paper_values['repo_vs_norepo']['mean_with_repo']:.2f})")
print(f"  Mean citations/year (Without Repo): {mean_without:.2f}  (paper: {paper_values['repo_vs_norepo']['mean_no_repo']:.2f})")

# T-test (one-sided: with repo > without repo)
t_stat2, t_p2 = stats.ttest_ind(cits_with_repo, cits_no_repo, alternative='greater')
print(f"\n  T-test:")
print(f"    T-statistic:  {t_stat2:.3f}")
print(f"    p-value:      {t_p2:.3f}   (paper: {paper_values['repo_vs_norepo']['t_test_p']:.3f})")
print(f"    Match:        {'YES' if abs(t_p2 - paper_values['repo_vs_norepo']['t_test_p']) < 0.05 else 'CLOSE' if abs(t_p2 - paper_values['repo_vs_norepo']['t_test_p']) < 0.1 else 'DIFFERS'}")

# Mann-Whitney U test (one-sided)
u_stat2, mw_p2 = stats.mannwhitneyu(cits_with_repo, cits_no_repo, alternative='greater')
print(f"\n  Mann-Whitney U test:")
print(f"    U-statistic:  {u_stat2:,.1f}")
print(f"    p-value:      {mw_p2:.3f}   (paper: {paper_values['repo_vs_norepo']['mannwhitney_p']:.3f})")
print(f"    Match:        {'YES' if abs(mw_p2 - paper_values['repo_vs_norepo']['mannwhitney_p']) < 0.05 else 'CLOSE' if abs(mw_p2 - paper_values['repo_vs_norepo']['mannwhitney_p']) < 0.1 else 'DIFFERS'}")

# Kruskal-Wallis H test (two-sided)
h_stat2, kw_p2 = stats.kruskal(cits_with_repo, cits_no_repo)
print(f"\n  Kruskal-Wallis H test:")
print(f"    H-statistic:  {h_stat2:.3f}")
print(f"    p-value:      {kw_p2:.3f}   (paper: {paper_values['repo_vs_norepo']['kruskalwallis_p']:.3f})")
print(f"    Match:        {'YES' if abs(kw_p2 - paper_values['repo_vs_norepo']['kruskalwallis_p']) < 0.05 else 'CLOSE' if abs(kw_p2 - paper_values['repo_vs_norepo']['kruskalwallis_p']) < 0.1 else 'DIFFERS'}")

# =========================================================================
# Summary Table
# =========================================================================
print("\n" + "=" * 70)
print("VALIDATION SUMMARY")
print("=" * 70)
print(f"{'Test':<40} {'Reproduced':<15} {'Paper':<15} {'Status'}")
print("-" * 85)

rows = [
    ("Mean cits/yr (Simulation)",      f"{mean_sim:.2f}",   f"{paper_values['sim_vs_nosim']['mean_sim']:.2f}"),
    ("Mean cits/yr (Non-Simulation)",   f"{mean_nosim:.2f}", f"{paper_values['sim_vs_nosim']['mean_nosim']:.2f}"),
    ("Sim vs NoSim: T-test p",         f"{t_p:.2e}",        f"{paper_values['sim_vs_nosim']['t_test_p']:.2e}"),
    ("Sim vs NoSim: Mann-Whitney p",   f"{mw_p:.2e}",       f"{paper_values['sim_vs_nosim']['mannwhitney_p']:.2e}"),
    ("Sim vs NoSim: Kruskal-Wallis p", f"{kw_p:.2e}",       f"{paper_values['sim_vs_nosim']['kruskalwallis_p']:.2e}"),
    ("Mean cits/yr (With Repo)",        f"{mean_with:.2f}",  f"{paper_values['repo_vs_norepo']['mean_with_repo']:.2f}"),
    ("Mean cits/yr (Without Repo)",     f"{mean_without:.2f}",f"{paper_values['repo_vs_norepo']['mean_no_repo']:.2f}"),
    ("Repo vs NoRepo: T-test p",       f"{t_p2:.3f}",       f"{paper_values['repo_vs_norepo']['t_test_p']:.3f}"),
    ("Repo vs NoRepo: Mann-Whitney p", f"{mw_p2:.3f}",      f"{paper_values['repo_vs_norepo']['mannwhitney_p']:.3f}"),
    ("Repo vs NoRepo: Kruskal-Wallis p",f"{kw_p2:.3f}",     f"{paper_values['repo_vs_norepo']['kruskalwallis_p']:.3f}"),
]

for label, reproduced, paper in rows:
    try:
        r = float(reproduced)
        p = float(paper)
        if p == 0:
            status = "MATCH" if r == 0 else "DIFFERS"
        elif abs(r) < 1e-10 and abs(p) < 1e-10:
            status = "MATCH"
        elif abs(r - p) / max(abs(p), 1e-300) < 0.05:
            status = "MATCH"
        elif abs(r - p) / max(abs(p), 1e-300) < 0.2:
            status = "CLOSE"
        else:
            status = "DIFFERS"
    except ValueError:
        status = "N/A"
    print(f"  {label:<40} {reproduced:<15} {paper:<15} {status}")

print("\nNote: Small differences are expected due to floating-point precision")
print("and potential minor dataset updates between paper submission and repository.")
