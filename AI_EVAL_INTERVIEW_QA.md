# How to Ace AI Eval Interview Questions — Q&A Study Guide

**Video:** [Hamel Husain — How to Ace AI Eval Interview Questions (for Engineers & PMs)](https://www.youtube.com/watch?v=6RTgIr08LMs)  
**Duration:** 21:18  
**Purpose:** Interview-preparation questions, answers, and worked examples derived from the video.

---

## 1. Interview format and mindset

### Q1. What does a typical AI-evals interview assessment look like?

Candidates are often given a dataset and about three or four hours, either as a take-home exercise or during an interview. They may need to inspect labeled and unlabeled examples, build or improve an agent, run evaluations, and explain their results and decisions.

**Timestamp:** [0:00](https://www.youtube.com/watch?v=6RTgIr08LMs&t=0s)

### Q2. What is the biggest mistake candidates make at the start?

They point a coding agent or LLM at the dataset and ask it to find or fix everything. This hides the candidate’s judgment and often misses deliberate traps in the data. AI tools can help, but the candidate must personally inspect the data, question assumptions, and explain decisions.

**Timestamp:** [0:00](https://www.youtube.com/watch?v=6RTgIr08LMs&t=0s)

### Q3. What abilities is the interviewer really testing?

The task tests more than model performance. It tests whether the candidate can:

- inspect messy data critically;
- detect weak labels and misleading metrics;
- design sensible experiments;
- avoid overfitting;
- reason about cost, latency, complexity, and product impact;
- communicate limitations clearly;
- use tools without surrendering their judgment.

---

## 2. Structuring the submission

### Q4. How should an AI-eval assessment be structured?

A strong submission should contain:

1. Executive summary
2. Data analysis
3. Experiments
4. Consolidated results
5. Learnings and limitations
6. Recommended next steps
7. Disclosure of AI tools used

**Timestamp:** [2:09](https://www.youtube.com/watch?v=6RTgIr08LMs&t=129s)

### Q5. What belongs in the executive summary?

In roughly one short paragraph—no more than about one-third of a page—state what was built, the principal result, and the recommended approach. It should let a busy reviewer understand the outcome without reading the entire report.

### Q6. Where should most of the available time go?

Spend roughly **50–70%** of the time understanding the data. Data analysis is the section many candidates skip, but it is often what best distinguishes someone who understands evaluation work from someone who merely runs benchmarks.

**Timestamp:** [2:47](https://www.youtube.com/watch?v=6RTgIr08LMs&t=167s)

---

## 3. Inspecting the data

### Q7. What data-quality problems should a candidate look for?

Look for:

- missing labels;
- inconsistent label formats;
- insufficient examples for important classes;
- ambiguous or poorly defined labels;
- inconsistent units;
- noisy or out-of-scope examples;
- class imbalance;
- labels that cannot support the requested metric;
- missing negative or failure cases.

Never assume that an interview dataset is correct or complete.

### Q8. Why can high accuracy be misleading?

Suppose every guardrail example is marked as valid and there are no policy-violating inputs. A classifier that always predicts “valid” gets 100% accuracy while providing no evidence that it can detect violations. The candidate should identify the missing class rather than celebrate the score.

**Timestamp:** [3:36](https://www.youtube.com/watch?v=6RTgIr08LMs&t=216s)

### Q9. How should missing classes or labels be handled?

First, document the gap. Then seek the strongest practical proxy:

1. trustworthy external data, if available;
2. manually labeled examples, when feasible;
3. synthetic examples for gaps such as guardrail failures;
4. an explicit limitation if none can be validated adequately.

Explain why the proxy is appropriate and where it may fail.

### Q10. Why is external data valuable in an interview?

It demonstrates resourcefulness and can provide a cleaner reference dataset when the supplied data is sparse or inconsistent. The external data can support development and validation while the supplied dataset remains the final test set. Its relevance, provenance, and limitations still need to be discussed.

**Timestamp:** [4:35](https://www.youtube.com/watch?v=6RTgIr08LMs&t=275s)

### Q11. When is synthetic data useful?

Synthetic data is useful when a critical class is absent—for example, non-tree images needed to test an image-input guardrail. It is better than ignoring the missing class, but it should be labeled as synthetic and treated as a proxy rather than unquestioned ground truth.

### Q12. What is an example of inconsistent labeling?

One species label might be simply `English oak`, while another contains `pine, long needles, orange bark`. Heights might appear as `12 m` in one row and `50` with no unit in another. A candidate should normalize what can be normalized, flag ambiguity, and explain any assumptions rather than silently comparing incompatible values.

**Timestamp:** [6:19](https://www.youtube.com/watch?v=6RTgIr08LMs&t=379s)

### Q13. How should out-of-scope or noisy examples be treated?

Decide whether the examples belong to the intended product domain. For instance, bonsai images may or may not fit a general tree-health application. Remove, separate, or retain them based on an explicit product decision, and document that choice.

---

## 4. Designing experiments

### Q14. How should each experiment be described?

For every experiment, state:

- **Goal:** what capability or hypothesis is being tested;
- **Method:** what changed from the baseline;
- **Metrics:** how performance is measured;
- **Findings:** what happened and why it matters;
- **Trade-offs:** quality, latency, cost, stability, and complexity.

**Timestamp:** [8:20](https://www.youtube.com/watch?v=6RTgIr08LMs&t=500s)

### Q15. Why is a simple baseline necessary?

A simple baseline—such as a basic prompt-only system—shows whether later complexity actually creates value. Without it, a candidate cannot demonstrate that retrieval, model changes, prompt tuning, or other techniques improve the system.

### Q16. What should an experiment table contain?

A useful table might include:

| Version | Change | Validation score | Test score | Cost | Latency | Notes |
|---|---|---:|---:|---:|---:|---|
| V1 | Prompt-only baseline | — | — | — | — | Simplest viable approach |
| V2 | Add retrieval | — | — | — | — | Tests value of external data |
| V3 | Change model | — | — | — | — | Tests model-quality trade-off |
| V4 | Automated prompt tuning | — | — | — | — | Check for real gain and overfitting |

The table should be followed by a short narrative explaining the important findings.

### Q17. Why should validation and test results be separated?

A large gap between validation and test performance may indicate overfitting. A method with an excellent validation score but a much lower test score is less trustworthy than a slightly weaker method whose results generalize consistently.

**Timestamp:** [10:54](https://www.youtube.com/watch?v=6RTgIr08LMs&t=654s)

### Q18. Should the highest-scoring experiment always win?

No. A slightly lower-scoring approach may be preferable if it is faster, cheaper, simpler, more stable, or less prone to overfitting. Selecting it demonstrates product judgment rather than benchmark maximization.

---

## 5. Challenging weak evaluation criteria

### Q19. What should a candidate do when the requested metric is poorly designed?

Compute the requested result so the assignment is fulfilled, but politely explain why the metric is weak and propose a better design. The criticism should be specific and reasoned, not dismissive.

**Timestamp:** [11:44](https://www.youtube.com/watch?v=6RTgIr08LMs&t=704s)

### Q20. Why is combining generic dimensions into one score risky?

A composite such as “helpfulness plus tone from 0 to 100” can hide distinct failures and may not be interpretable or actionable. Separate criteria tied to observable behavior are more useful—for example:

- Is the image sufficient for assessment?
- Is the advice grounded in visible evidence?
- Does watering advice request or account for soil moisture?
- Does the response avoid blame or scolding?
- Does it clearly communicate uncertainty?

### Q21. How can a candidate disagree with the interviewer constructively?

Honor the requested task first, then explain:

1. the problem with the requested approach;
2. the risk it creates;
3. the alternative evaluation design;
4. why the alternative is more actionable or valid.

This can either avoid a deliberate trap or teach an interviewer who has less eval experience.

---

## 6. Results, learnings, and next steps

### Q22. How should the final results section differ from the experiment section?

The experiment section records individual trials. The results section synthesizes them into a recommended system: the winning combination, improvement over baseline, final scores across capabilities, and the cost/latency/complexity trade-offs that justify the recommendation.

**Timestamp:** [13:39](https://www.youtube.com/watch?v=6RTgIr08LMs&t=819s)

### Q23. What should appear in the learnings and limitations section?

Summarize:

- what worked and why;
- what failed or added no value;
- signs of overfitting;
- weaknesses in the supplied data;
- unvalidated LLM-as-judge outputs;
- assumptions made because human labels were unavailable;
- evaluation criteria that should be redesigned.

This section should show both insight and humility.

**Timestamp:** [15:17](https://www.youtube.com/watch?v=6RTgIr08LMs&t=917s)

### Q24. What makes a strong next-steps section?

Make concrete recommendations rather than saying only “get better data.” Specify:

- which examples or labels are missing;
- how they should be collected or annotated;
- which slices need deeper testing;
- what product changes could make outputs safer or easier to evaluate;
- which experiments should be run next and why.

**Timestamp:** [17:06](https://www.youtube.com/watch?v=6RTgIr08LMs&t=1026s)

---

## 7. Audience Q&A

### Q25. How do interview experiments differ from production A/B tests?

In this interview format, candidates will usually receive a fixed dataset and be asked to compute evaluations and metrics. Unless the role is specifically data-science-oriented, they generally do not need to design or run a live A/B test.

**Timestamp:** [18:17](https://www.youtube.com/watch?v=6RTgIr08LMs&t=1097s)

### Q26. Should results be presented in a custom UI?

Only if requested or clearly useful. Follow the required format—such as a PDF or GitHub repository—before adding presentation layers. A thoughtful, readable report is better than an elaborate but unclear AI-generated interface or slide deck.

**Timestamp:** [18:35](https://www.youtube.com/watch?v=6RTgIr08LMs&t=1115s)

### Q27. What is expected from product managers?

PM candidates are less likely to be tested on calculations such as F1 score, but they may still receive a dataset and may be asked to write some code. Their main opportunity is to demonstrate careful data inspection, nuanced product judgment, sensible evaluation design, and clear communication.

**Timestamp:** [19:11](https://www.youtube.com/watch?v=6RTgIr08LMs&t=1151s)

### Q28. Can candidates use coding agents and eval tools?

Yes—using tools demonstrates resourcefulness. However, the candidate must remain the author of the reasoning. A report that merely reflects an agent’s generic output will resemble everyone else’s and fail to showcase distinctive judgment.

**Timestamp:** [19:45](https://www.youtube.com/watch?v=6RTgIr08LMs&t=1185s)

---

## 8. Worked examples: Tree Buddy take-home

The examples below use the video's hypothetical **Tree Buddy** application: a user uploads a tree photo, and the system checks the input, identifies the species, assesses health, and recommends care.

### Example 1: Executive summary

> I evaluated a Tree Buddy pipeline for input safety, species identification, health findings, and care recommendations. The supplied dataset contained 120 images, but it had no negative guardrail examples, inconsistent height units, and sparse age labels. I established a prompt-only baseline, added curated tree-data retrieval, and compared two models. Retrieval improved species accuracy from 71% to 84%, while the larger model reached 86% but doubled latency and tripled estimated cost. I recommend the retrieval-based mid-sized model because it offers the best quality–cost trade-off. Before launch, I would collect real non-tree inputs and validate the health and tone rubrics against expert human labels.

Why this works: it states the task, exposes the main data limitations, reports the result, makes a recommendation, and names the most important next step.

### Example 2: Data audit

| Finding | Evidence | Risk | Action taken |
|---|---|---|---|
| No negative guardrail examples | 120/120 inputs marked valid | A model that always accepts gets 100% accuracy | Created 40 synthetic non-tree inputs and reported them separately |
| Sparse health labels | 96/120 rows labeled | Aggregate health score may be biased | Evaluated health only on labeled rows; reported coverage |
| Sparse age labels | 8/120 rows labeled | Accuracy would be unstable and misleading | Excluded age from headline metrics |
| Inconsistent height units | Values include `12 m`, `50`, and blanks | Exact-match evaluation becomes invalid | Normalized explicit units; marked unitless values unknown |
| Mixed species-label format | `English oak` vs. `pine, long needles, orange bark` | Labels combine class and description | Split species from descriptive attributes |
| Possible domain ambiguity | Dataset includes bonsai trees | Unclear whether these are supported inputs | Reported bonsai as a separate evaluation slice |

**Example write-up:**

> I did not treat the dataset as ground truth without inspection. In particular, the guardrail column contains only one class, so its apparent 100% baseline accuracy is non-informative. I created a separate synthetic challenge set to test obvious rejection behavior, but I do not treat that set as a substitute for real user failures.

### Example 3: Synthetic guardrail cases

| Input | Expected outcome | Reason |
|---|---|---|
| Clear photo of one oak tree | Accept | In-domain input |
| Photo of a dog | Reject | No tree present |
| Screenshot containing only text | Reject | Not a usable tree image |
| Tree mostly hidden behind a building | Ask for another photo | Tree present, but evidence is insufficient |
| Bonsai tree | Product-policy dependent | Requires an explicit scope decision |
| Tree photo containing a person | Accept or reject based on privacy policy | Tests whether policy is defined clearly |

The final two examples are useful because they reveal product ambiguity instead of forcing every case into a simplistic pass/fail label.

### Example 4: Experiment definition

**Goal:** Improve species identification without unacceptable cost or latency.

**Hypothesis:** Retrieving similar labeled trees will improve identification more efficiently than switching to the largest model.

**Baseline:** Mid-sized vision model with a zero-shot prompt.

**Variants:**

1. Add three-shot examples.
2. Retrieve the five most similar records from a curated tree dataset.
3. Replace the mid-sized model with a larger model.
4. Combine retrieval with the larger model.

**Metrics:** Macro F1 across species, accuracy on rare species, p95 latency, and estimated cost per 1,000 requests.

**Decision rule:** Prefer the simplest variant within two percentage points of the best test score, unless a lower-scoring model fails a safety-critical slice.

### Example 5: Completed experiment table

> The numbers below are illustrative examples, not results reported in the video.

| Version | Method | Validation F1 | Test F1 | p95 latency | Cost / 1K | Decision |
|---|---|---:|---:|---:|---:|---|
| V1 | Prompt-only baseline | 0.72 | 0.71 | 1.2 s | $4 | Baseline |
| V2 | Three-shot prompt | 0.76 | 0.74 | 1.3 s | $5 | Small gain |
| V3 | Retrieval + mid-sized model | 0.85 | 0.84 | 1.8 s | $7 | **Recommended** |
| V4 | Larger model only | 0.88 | 0.86 | 3.9 s | $21 | Higher score, poor trade-off |
| V5 | Automated prompt tuning | 0.94 | 0.73 | 1.4 s | $6 | Likely overfit |

**Example interpretation:**

> V4 achieved the highest test F1, but V3 was only two points lower while being approximately three times cheaper and substantially faster. V5’s 21-point validation–test gap suggests overfitting. I therefore recommend V3, subject to slice-level safety checks.

### Example 6: Replacing a vague composite metric

**Requested metric:** “Grade helpfulness and tone from 1–5, then combine them into a score from 0–100.”

**Problem:** A single score can hide severe failures. A polite but fabricated diagnosis could outrank a cautious, grounded answer.

**Better rubric:**

| Criterion | Type | Example pass condition |
|---|---|---|
| Image sufficiency | Binary | The full relevant tree area is visible |
| Diagnostic grounding | 0–2 | Every health claim cites visible evidence |
| Advice safety | Binary gate | No harmful or unjustified treatment advice |
| Actionability | 0–2 | Gives a specific, feasible next action |
| Uncertainty | Binary | States uncertainty when evidence is insufficient |
| Tone | Binary | Avoids blame, scolding, or alarmism |

**Example critique to an interviewer:**

> I calculated the requested composite score for comparability. I would not use it as the production gate, because it can conceal a safety failure behind strong tone or helpfulness ratings. I would keep the dimensions separate and make advice safety a required pass condition.

### Example 7: Evaluating a response

**Model response:**

> The brown leaf edges mean your tree is drought-stressed. Give it extra water this week. It is clear that you have been neglecting your tree.

**Evaluation:**

- **Grounding:** Fail — brown edges may have several causes.
- **Image sufficiency:** Unknown — the photo may not show enough of the tree or soil.
- **Action safety:** Fail — recommending extra water without checking soil moisture may cause harm.
- **Tone:** Fail — “you have been neglecting” is accusatory and unsupported.
- **Uncertainty:** Fail — the diagnosis is stated as certain.

**Improved response:**

> Brown leaf edges can be associated with water stress, heat, salt buildup, or root problems, but the photo alone is not enough to confirm the cause. Check whether the top few centimetres of soil are dry and look for similar browning across the tree. If possible, upload a full-tree photo and a close-up of the leaves before changing the watering schedule.

### Example 8: Learnings and limitations

> Retrieval improved identification for common species, but gains were smaller for rare species because the reference dataset had poor coverage. Automated prompt tuning improved validation performance but did not generalize to the held-out test set. The synthetic guardrail set established basic rejection behavior but may not represent real misuse. Health recommendations were scored by an LLM judge without expert calibration, so those scores should be considered directional rather than definitive.

### Example 9: Specific next steps

Weak recommendation:

> Get better data and improve the model.

Strong recommendation:

> Collect at least 50 real examples for each high-risk input class: non-tree images, unreadable photos, multiple trees, screenshots, and privacy-sensitive images. Ask two arborists to label diagnosis grounding and advice safety, then adjudicate disagreements into a written rubric. Add rare-species coverage to the retrieval corpus and re-run the evaluation by species frequency, image quality, and geographic region. In the product, guide users to capture one full-tree image plus a leaf close-up before generating care advice.

### Example 10: AI-tool disclosure

> I used a coding assistant to generate exploratory scripts and refactor plotting code. I manually inspected the dataset, defined the evaluation slices, reviewed generated code, and verified all reported metrics. I used an LLM to draft synthetic guardrail examples, which are identified separately from human- or source-labeled data. No LLM-generated label was treated as validated ground truth.

---

## Rapid-review checklist

Before submitting an AI-eval interview assignment, verify that you can answer **yes** to each question:

- [ ] Did I inspect the raw data rather than trusting its labels?
- [ ] Did I identify missing classes, ambiguous labels, inconsistent units, and noise?
- [ ] Did I explain every filtering, normalization, and labeling decision?
- [ ] Did I establish a simple baseline?
- [ ] Did I separate validation and test results?
- [ ] Did I compare approaches on quality, cost, latency, stability, and complexity?
- [ ] Did I check for overfitting?
- [ ] Did I challenge weak metrics constructively while still completing the task?
- [ ] Did I recommend a system rather than merely list scores?
- [ ] Did I state what worked, what failed, and what remains uncertain?
- [ ] Did I propose specific data and product improvements?
- [ ] Did I disclose the AI tools I used?
- [ ] Does the final report clearly show my own judgment?

---

## One-sentence takeaway

**The strongest AI-eval interview submission is not the one with the highest score; it is the one that demonstrates critical data inspection, well-designed experiments, sound trade-off decisions, transparent limitations, and independent judgment.**