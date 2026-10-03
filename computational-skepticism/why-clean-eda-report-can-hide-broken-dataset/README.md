# Why a Clean EDA Report Can Hide a Broken Dataset

A dataset passes every standard check — no missing values, well-behaved distributions, and zero outliers — yet still completely breaks the production model built on it.

In this episode of *Computational Skepticism for AI*, Professor Bear and Liam explain why exploratory data analysis (EDA) can look immaculate while hiding a catastrophic data loss: when upstream joins silently drop rows (such as non-matching legacy identifiers), the surviving records show zero missingness simply because dropped rows never made it into the table. Standard EDA diagnostics read only the survivors and call them the world.

---

### Key Takeaways & Carry-Out
- **The Core Mechanism**: In a multi-table merge, non-matching records (e.g. 4% of rows due to legacy identifier formatting) fail the join and silently vanish before reaching the analysis table.
- **The Epistemic Blindspot**: You cannot compute the missingness of rows that never made it into the dataset. The EDA diagnostic lens inspects only the surviving rows.
- **Carry-Out Law**: You cannot compute the missingness of rows that never made it into the dataset — every diagnostic reads only the survivors and calls them the world.
- **Direction A**: A spotless exploratory data analysis report is NOT proof that your dataset is complete.
- **Direction B**: Exploratory analysis is NOT useless — it reliably catches corrupt types, impossible values, and internal distribution skew within the table's perimeter.

---

### Your Turn — Prompt for Claude / AI Assistants
```
Take an assembled dataset in your current pipeline. Before running any summary statistics, trace its row count back to the original source tables. Calculate the exact drop rate at every join, and check if dropped records cluster in a specific subpopulation.
```

---

### Metadata
- **Series**: Computational Skepticism for AI
- **Channel**: @HumanitariansAI (youtube.com/@HumanitariansAI)
- **Playlist**: Computational Skepticism — Data & Model Validation
- **Source**: *Computational Skepticism for AI* by Nik Bear Brown (Chapter 3: Data Validation: Reconstructing the Epistemic Frame Behind a Dataset)
- **Voice**: Liam (synthesized via open-weights Kokoro `am_onyx`)
- **Visuals**: Manim + Remotion (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Code (no media)**: https://github.com/nikbearbrown/humanitarians-youtube/tree/main/computational-skepticism/why-clean-eda-report-can-hide-broken-dataset
