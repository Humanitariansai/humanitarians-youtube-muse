# CAJAL Figure Report — 23 ShipIt: Interface Design and Deployment

Source chapter: chapters/23-shipit-interface-and-deployment.md
Chapter slug: 23-shipit-interface-and-deployment

---

## FIGURE 1 · The four interface layers · Critical · structural schematic
The taxonomy that opens the chapter: interface is not "UI". Four stacked layers — visual surface, interaction model, deployment surface, brand surface — each card naming what it includes, the common engineering mistake, and the failure mode when misaligned. The Bard failure lived in Layer 4, the one engineers underinvest in.
- Spatial: four horizontal layers stacked top-to-bottom (Layer 1 top), each a band with layer name, "includes:" line, and "mistake:" tag; the brand-surface band annotated as where Bard failed.
- RED: none — four layers that must all be coherent; a neutral taxonomy. (The Bard note is text, not a red mark.)
- EXCLUSIONS: no three-misalignment-types content, no case studies, no Streamlit/Gradio material, no audit table.

## FIGURE 2 · Three faces of misalignment · Critical · comparison panels
The three structural ways an interface contradicts its brand: confidence (output looks more certain than the system is), capability (interface implies abilities the tool lacks), tone (voice the system cannot maintain). Three panels — definition, how engineers produce it, what users experience, the fix. The diagnostic frame before the case studies apply it.
- Spatial: three equal panels across; each with type name, one-line definition, "engineers cause it by…", "user experiences…", and "fix:" in the secondary register.
- RED: the confidence-misalignment panel — the chapter names it the most common failure for engineer-built AI interfaces; the one the reader is most likely to commit. (Single red mark.)
- EXCLUSIONS: no Bard/Snapchat/Tay case detail (that is Fig 3), no four-layer taxonomy, no framework comparison.

## FIGURE 3 · Three case studies mapped to three misalignments · Important · comparison table
Bard (confidence), Snapchat (tone), Tay (capability) — each row carrying interface promise, system reality, and brand consequence, mapped to its misalignment type. A directed comparison that makes the three failures immediately comparable and ties theory to real, fast brand damage.
- Spatial: three-row table, columns Product/event | Misalignment type | Interface promise | System reality | Brand consequence; each row tagged with its type.
- RED: none — three peer cases illustrating one structure; neutral reference.
- EXCLUSIONS: no $100B/petition figures presented as the focus (mention only as consequence text), no four-layer taxonomy, no audit content.

## FIGURE 4 · Streamlit vs. Gradio selection guide · Important · comparison panels
The framework choice reframed as an interaction-model decision: do work (Streamlit) vs. try the model (Gradio). Two columns — user's primary job, interaction model implied, architecture fit, deployment platform, which pipeline types fit. Plus the mismatch to avoid: orchestrated system behind a free-form Gradio box. A lookup, not a debate.
- Spatial: two-column table, Streamlit left / Gradio right, five aligned criterion rows; a footer warning band naming the mismatch to avoid.
- RED: none — two peer tools chosen by fit; the decision is a lookup, not an endorsement.
- EXCLUSIONS: no interface-layer taxonomy, no misalignment types, no deployment steps, no code.

## FIGURE 5 · Minimum viable interface — required vs. prohibited · Critical · comparison panels
The build spec: three required components (input affordance matching system scope, visible processing state, output surface representing confidence) versus three prohibited (features the system can't reliably support, input types it can't handle, capability claims it can't keep). The alignment audit sits as the gate between design and deploy.
- Spatial: two columns — "REQUIRED" left (3 boxes), "PROHIBITED" right (3 boxes); a horizontal gate band beneath labeled "alignment audit — the gate between design and deploy" with an arrow to "deploy".
- RED: the alignment-audit gate band — the single checkpoint the chapter insists must be passed before shipping; the thing the reader must not skip. (Single red mark.)
- EXCLUSIONS: no worked audit rows (that is Fig 6), no framework comparison, no README checklist, no case studies.

## FIGURE 6 · The alignment audit, worked · Important · comparison table
The two-column exercise in action on the sentiment pipeline: five interface claims, the system reality for each, pass/fail, and the specific fix applied. Three of five needed narrowing — none required changing the system, all required presenting the realistic case. The audit format made concrete.
- Spatial: five-row table, columns Claim as written | System reality | Pass/Fail | Fix applied; pass rows marked with a check, fail rows with the narrowed-claim rewrite.
- RED: none — a neutral worked example; the pass/fail marks are glyphs, not color emphasis.
- EXCLUSIONS: no required/prohibited component duplication, no deployment steps, no archetype mapping.

## FIGURE 7 · Deployment in four steps · Supplementary · process flowchart
The gate to a shareable URL: choose a host → write requirements.txt (clean venv) → handle secrets correctly → test the deployed URL as a first-time user. Each step annotated with its most common failure (missing deps, keys in the repo). The unglamorous but mandatory path from working code to public artifact.
- Spatial: four boxes left-to-right with forward arrows; each step numbered with a one-line failure-mode note beneath; terminal node "public URL someone else can use".
- RED: none — a neutral procedural checklist; four sequential peer steps.
- EXCLUSIONS: no README checklist (that is Fig 8), no framework comparison, no interface-layer taxonomy.

## FIGURE 8 · The README as the last interface layer · Supplementary · structural schematic
The README reframed as interface, not documentation: six elements — what it does, how to use it, limits (the README-level alignment audit), architecture diagram, tech stack, deployed URL at the top. Each element with its common failure mode. The final surface the user checks before deciding to use the tool.
- Spatial: six stacked element rows in README reading order (URL at top), each with element name, "should contain" line, and a "fails when…" tag; a left rule marking it as one document.
- RED: none — six peer elements of one artifact; neutral checklist.
- EXCLUSIONS: no deployment steps duplication, no audit table, no archetype-interface mapping, no case studies.

---

## Video candidates

FIGURE the-four-interface-layers — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a spatial cross-section or structural schematic whose value lies in inspecting all parts simultaneously.
FIGURE three-faces-of-misalignment — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE three-case-studies-mapped-to-three-misalignments — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE streamlit-vs.-gradio-selection-guide — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE minimum-viable-interface-—-required-vs.-prohibited — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE the-alignment-audit,-worked — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE deployment-in-four-steps — Status: VIDEO CANDIDATE · Criterion: 2 · Reason: a sequence of causal steps: the student must witness each stage causing the next to understand the mechanism, not merely see the endpoints.
FIGURE the-readme-as-the-last-interface-layer — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a spatial cross-section or structural schematic whose value lies in inspecting all parts simultaneously.

**Chapter recommendation:** **deployment-in-four-steps** — the sole video candidate; a sequence of causal steps: the student must witness each stage causing the next to understand the mechanism, not merely see the endpoints.
