*Date: 2026-09-13. Research note — expert opinion + Bayesian approaches to theism.*

## 1. Survey data

### PhilPapers Survey — professional philosophers

**2009** (N=3226 total; 1803 faculty/PhD, 829 grad students, target faculty in 99 leading anglophone departments):
- Atheism: accept/lean 72.8% (faculty subset: 73%)
- Theism: accept/lean ~16% (faculty subset: ~15%)
- Agnostic/other/undecided: ~6%
- Grad students only: 64% atheism, 21% theism (less atheist than faculty — inference: selection/attrition or generational effect, not confirmed by the survey itself)

**2020** (~2000 respondents, wider sampling than 2009 — Bourget & Chalmers explicitly warn against naive trend-reading between the two waves because the sampled population changed):
- Theism: accept/lean **18.93%**
- Atheism: accept/lean **66.95%**
- Other/agnostic/insufficiently familiar: **~14.1%** (remainder)

So atheism outnumbers theism roughly 3.5:1 among philosophers generally, in both waves, with a modest theism uptick and atheism dip 2009→2020 that the authors caution against over-reading causally.

**The philosophy-of-religion split (both years show this, 2020 numbers are cited most precisely):**
- AOS (area of specialization) = philosophy of religion: **78% theism** among specialists
- Non-specialists: **17% theism**
- This is the single largest "specialist effect" in the entire 2020 survey (100 questions) — larger than any other subfield divergence. The closely linked fine-tuning question shows the same pattern: 74% of phil-of-religion specialists favor "design" as the explanation for fine-tuning vs. 13% of non-specialists.
- 2009 wording was similar: ~72.3% theism among phil-of-religion specialists vs. ~19% atheism among that same group — i.e., the split is not new to 2020, it's a stable feature across both survey waves.

Sources:
- Bourget, D. & Chalmers, D. "Philosophers on Philosophy: The 2020 PhilPapers Survey" — https://philarchive.org/archive/BOUPOP-3 (also https://journals.publishing.umich.edu/phimp/article/id/2109/print/)
- Raw results: https://survey2020.philpeople.org/survey/results/4842
- PhilPapers Surveys hub (both waves): https://philpapers.org/surveys/
- Secondary summary/discussion of specialist effect: https://dailynous.com/2015/01/30/why-are-so-many-philosophers-of-religion-theists/ (2009-era piece, framing is still current)

### Scientists

**Larson & Witham, *Nature* 1998** — replication of Leuba's 1914/1933 surveys, sent to 517 members of the US National Academy of Sciences (biological + physical scientists, incl. mathematicians, physicists, astronomers):
- Belief in a personal God: **7%** of NAS members (down from ~27.7% in Leuba's 1914 "greater scientists" sample, and from a 1996 rank-and-file scientist replication of ~39.3%)
- By discipline: biological scientists lowest (5.5% belief in God), physicists/astronomers ~7.5%, mathematicians highest at 14.3%
- Interpretation: this is the most elite tier (NAS membership), not "scientists" broadly — selection into NAS itself may correlate with disbelief, so don't generalize this 7% to all scientists.
- Source: Larson, E.J. & Witham, L. "Leading scientists still reject God." *Nature* 394, 313 (1998). Secondary write-ups: https://ncse.ngo/do-scientists-really-reject-god , https://dsimanek.vialattea.net/sci_relig.htm

**Pew Research 2009** — survey of 2,533 AAAS (American Association for the Advancement of Science) members, a much broader/less elite population than NAS:
- Belief in God: **33%**
- Belief in "universal spirit or higher power" (non-personal): **18%**
- Combined belief in some deity/higher power: **51%**
- No belief in either: **41%**
- Comparison, US general public (Pew 2007/2009-era): 83% believe in God, 95% believe in some deity/higher power
- Source: https://www.pewresearch.org/religion/2009/11/05/scientists-and-belief/

**Takeaway on the scientist data:** the NAS (7%) vs AAAS (33% belief in God) gap is large and tracks *prestige/elite-selection*, not "science" as a monolithic category — flag this as an inference, but a fairly safe one given it's the most obvious confound between the two samples.

## 2. Why philosophers of religion skew theist — selection effect vs. evidence

Draper, P. & Nichols, R. "Diagnosing Bias in Philosophy of Religion." *The Monist* 96(3), 2013, 420–446. https://www.pdcnet.org/monist/content/monist_2013_0096_0003_0420_0446 (open-access version: https://www.ryantatenichols.com/writing/articles/diagnosing-bias-in-philosophy-of-religion-pdf)

Core argument:
- The subfield shows symptoms of poor epistemic health: too partisan, too polemical, too narrow, and too often judged by theological/religious criteria rather than philosophical ones.
- Two supporting lines: (a) cognitive-bias literature (motivated reasoning, confirmation bias) applies especially hard here because the subject matter is emotionally and identity-laden; (b) social/evolutionary psychology of religious *coalitional* behavior — religion recruits in-group loyalty mechanisms that bias inquiry toward defending the in-group's prior commitments.
- Mechanism for the 78/17 split: philosophy of religion, as a subfield, disproportionately attracts and retains people who are already religious (many PoR departments/programs have historical ties to seminaries or religiously-affiliated universities; people choose the subfield in part *because* they already care about defending or exploring their faith). This is a **selection effect into the specialty**, not evidence that studying the arguments in depth makes theism more credible.

**Effect on the evidential value of the 78% figure:** if selection dominates, 78%-theism-among-specialists is much weaker evidence for theism than a naive "trust the experts" heuristic would suggest — it's closer to "editors of a Catholic theology journal are mostly Catholic" than "epidemiologists mostly agree vaccines work." The correct comparison class for "philosophers who evaluate arguments about God" without motivated selection is arguably closer to the general philosopher population (66.95% atheism) or to closely adjacent unbiased-selection subfields (philosophy of science, metaphysics) than to self-selected philosophers of religion.

Counter-consideration (steelman, not sourced to a specific paper I fetched — flag as reasoned inference): one could argue selection effects run the other way for the *general* philosopher population too — professional philosophy as a field selects for people comfortable with metaphysical skepticism and naturalism from analytic training, so 66.95% atheism isn't a bias-free baseline either. Draper & Nichols's paper is itself aimed at PoR specifically; I did not find them making a symmetric claim about analytic philosophy's own selection effects toward naturalism. This symmetry point is my inference, not drawn from a source — treat it as a consideration to weigh, not a settled counter-finding.

## 3. Bayesian approaches — structure and critiques

**General Bayesian structure of the God question:**
```
P(God | E) = P(E | God) × P(God) / P(E)
```
The whole debate is a fight over three quantities: the **prior** P(God), the **likelihoods** P(E|God) vs P(E|¬God) for each piece of evidence E (fine-tuning, consciousness, religious experience, moral order, evil, resurrection testimony, etc.), and how independent pieces of evidence combine.

### Swinburne, *The Existence of God* (2nd ed. 2004)

- Explicitly Bayesian/inductive cumulative-case structure across ~11 factors (existence of a universe, its order/laws, fine-tuning, consciousness, morality, religious experience, miracles/resurrection, etc.)
- Conclusion: probability of theism is **>0.5** given the cumulative evidence (i.e., theism is "more probable than not"). In a separate, later argument (*The Resurrection of God Incarnate*, 2003) he calculates the probability of Jesus's resurrection specifically at **~97%**, using the same Bayesian scaffolding — this is the "97%" figure that gets popularly cited and is often mistakenly conflated with "97% probability God exists" (they are different claims: the resurrection number is conditional on prior natural-theology arguments already having raised the probability of theism substantially).
- **Key mechanism: simplicity as a truth-indicator for the prior.** Swinburne argues theism has a *high intrinsic prior probability* because "God" (an omnipotent, omniscient, perfectly free, single immaterial substance) is metaphysically the *simplest* possible explanatory hypothesis for the universe's existence — simpler than any naturalistic alternative with brute contingent laws/constants. He treats simplicity as an a priori guide to (intrinsic, not epistemic) probability, borrowed from a Bayesian-cum-Swinburnian confirmation theory he's developed since *An Introduction to Confirmation Theory* (1973) and *Epistemic Justification* (2001).

**Why widely criticized:**
1. **Numerical spuriousness (Gwiazda and others):** Swinburne's probabilities are not derived from any empirical frequency or agreed formal procedure — they're subjective/intrinsic probability judgments dressed in Bayesian notation, which creates false precision. Critics: there's no principled way to get from "God is simple" to a specific number like 0.5 or 0.97; the math looks rigorous but the priors are stipulated.
2. **Simplicity is contestable in the other direction (Dawkins/Sober):** Dawkins's "Ultimate 747 Gambit" (*The God Delusion*, 2006) argues an entity that is omniscient (monitors every particle, every thought, every prayer simultaneously) is definitionally *maximally complex* by any standard information-theoretic measure, not simple — postulating such a being to explain complexity is explanatorily backwards ("who designed the designer?"). Swinburne's reply is that simplicity should be assessed at the level of *number of independent substances/properties postulated* (one substance, few properties) rather than the *information content* of what that substance can do — critics find this move ad hoc, since it lets any sufficiently unified being count as "simple" regardless of its causal powers.
3. **Sober's independent critique** (*Evidence and Evolution*, 2008, applied more generally to design-type inference, not exclusively theism): likelihood-based reasoning about a "designer" requires independent knowledge of the posited designer's goals and abilities to generate any predictions at all — without that, P(E|design hypothesis) can't be non-arbitrarily specified, so the whole likelihood ratio is undefined rather than favorable. This is a structural objection to fine-tuning/design-style Bayesian arguments generally (theistic versions included), independent of Dawkins's complexity point.
4. **Coherence objection:** some critics (noted across multiple reviews) argue the classical-theist concept of God (omnipotent + omniscient + perfectly free + morally perfect + eternal + immaterial-yet-causally-active) may not even be a coherent hypothesis, which would make assigning it *any* probability, let alone a specific number, a category error prior to any Bayesian machinery.

Sources: https://www.diva-portal.org/smash/get/diva2:208388/FULLTEXT01.pdf (Gwiazda's critique); https://en.wikipedia.org/wiki/The_Existence_of_God_(book); https://en.wikipedia.org/wiki/Ultimate_Boeing_747_gambit; Sober, E. *Evidence and Evolution: The Logic Behind the Science* (Cambridge, 2008), reviewed at https://ndpr.nd.edu/reviews/evidence-and-evolution-the-logic-behind-the-science/ and https://arxiv.org/pdf/1004.5074

### Draper, Paul — evidential argument from evil (Bayesian)

- "Pain and Pleasure: An Evidential Problem for Theists" (*Noûs*, 1989) — canonical modern Bayesian argument *against* theism, structurally mirroring Swinburne's method but running it the other way.
- Compares Theism (T) against the **Hypothesis of Indifference (HI)**: any supernatural being(s), if they exist, are indifferent to sentient suffering.
- Claim: the observed distribution and biological function of pain/pleasure (tightly correlated with reproductive fitness, not with moral desert) is far more probable under HI than under T — i.e., P(E|HI) >> P(E|T) — which by Bayes drives down P(T|E) relative to P(HI|E), regardless of priors, as long as the evidential gap is large enough.
- Also developed a "decisive priors" line comparing theism to naturalistic alternatives (e.g., an "axiarchist"/"anaxiarchism"-style hypothesis) that fits the data at least as well while carrying a much lower ontological cost/higher prior plausibility.
- Significance: shows the Bayesian cumulative-case method is symmetric — it's a tool, not inherently theism-favoring; Draper uses the identical apparatus Swinburne uses and gets the opposite sign.

Source: https://philpapers.org/rec/DRATEP ; discussion at https://infidels.org/library/modern/paul-draper-serious/

### Philipse, Herman — *God in the Age of Science? A Critique of Religious Reason* (Oxford, 2012)

- Takes Swinburne's Bayesian cumulative case specifically as the *strongest* available case for theism ("if this fails, weaker arguments fail worse") and subjects it to sustained critique.
- Three-part conclusion:
  1. Theism, on inspection, **cannot be stated meaningfully** in a way that gives it determinate truth-conditions (a semantic/verificationist-flavored objection — echoes older logical-positivist worries about God-talk, but argued afresh).
  2. Even granting meaningfulness, theism as stated has **no genuine predictive power** over the evidence Swinburne cites — so the Bayesian likelihoods P(E|theism) can't actually be non-arbitrarily computed, meaning the whole Bayesian argument never gets off the ground (structurally similar to Sober's objection above, applied specifically to Swinburne).
  3. Even granting the whole method works as Swinburne intends, correctly run the numbers favor **atheism over theism**, not the reverse.
- Reviewed at: https://ndpr.nd.edu/reviews/god-in-the-age-of-science-a-critique-of-religious-reason/ ; publisher page: https://global.oup.com/academic/product/god-in-the-age-of-science-9780199697533

### Sobel, Jordan Howard — *Logic and Theism: Arguments For and Against Beliefs in God* (Cambridge, 2004)

- Comprehensive, highly technical survey covering ontological arguments (Anselm through Gödel's modal ontological proof), cosmological arguments (Aquinas, Leibniz), design/miracle arguments, and Pascalian wagers — using symbolic logic and Bayesian confirmation theory throughout.
- Verdict: judges essentially **all** classical theistic arguments unsound, and argues the "perfect being" concept of God is internally **incoherent** (a stronger claim than merely "unproven" — it's a claim that the target hypothesis is broken pre-evidentially).
- Also argues the (logical, not merely evidential) problem of evil succeeds in disproving the God of classical theism as standardly defined (omni-everything).
- Engaged with cumulative-case reasoning explicitly, including how to handle non-independence when "dividing the evidence" across multiple sub-arguments in a Bayesian framework (see §4 below) — Sobel's reply-to-critics piece addresses Swinburne directly: https://philapers.org/rec/SOBTMC-2 (find via https://philpapers.org/rec/SOBTMC-2)
- Notable: reception was positive across both theist and atheist philosophers, i.e., regarded as a rigorous rather than polemical treatment — for calibration purposes this is one of the more "trusted by both camps" technical sources in the whole literature.

Sources: https://infidels.org/library/modern/theodore-drange-sobel/ (review) ; https://www.reasonablefaith.org/writings/scholarly-writings/the-existence-of-god/sobels-acid-bath-for-theism-review-article-logic-and-theism (a hostile-but-detailed review from a theist commentator, useful for seeing what a critic concedes)

## 4. Does the cumulative case actually accumulate?

Formal point: if you have *n* independent pieces of evidence each with likelihood ratio *k* in favor of a hypothesis, the combined posterior odds multiply: starting odds × k₁ × k₂ × ... × kₙ. E.g., starting at 2:1 with five independent pieces of evidence each carrying a modest 2.5:1 likelihood ratio compounds to roughly 3125:1 — this is the mathematical fact that makes "cumulative case" arguments look powerful even when no single argument is individually decisive (Swinburne leans on this explicitly across his ~11 factors).

**When this fails / conditions for failure:**
1. **Non-independence.** The multiplication step is only valid if the pieces of evidence are probabilistically independent *given each hypothesis*. Many of Swinburne's factors are not independent: e.g., "religious experience," "existence of moral order," and "existence of consciousness" all draw on a shared background picture of humans as specially significant, and updating on one plausibly shifts your assessment of the others' evidential weight too. If evidence is correlated, naively multiplying likelihood ratios **double-counts** and inflates the final posterior — this is one of the most common formal errors cumulative-case critics point to (flagged in the "dividing the evidence" literature Sobel engages with, and it's a standard Bayesian-network point about conditional vs. marginal independence, not something unique to theism).
2. **Priors swamp small likelihood ratios in the other direction.** If P(theism) starts very low (e.g., because of a strong simplicity- or parsimony-based prior favoring naturalism, or because the concept is judged incoherent per Philipse/Sobel), a handful of weak-to-moderate likelihood ratios (2:1, 3:1 each) may be nowhere near enough to overcome a prior of, say, 1000:1 against — cumulative cases can't rescue a hypothesis whose prior is bad enough, no matter how many weakly-favorable data points you stack, unless at least some individual ratios are large.
3. **Mixed-sign evidence.** A cumulative *case* only works if you're cherry-picking only the theism-favoring items into the sum. A properly symmetric Bayesian treatment must also fold in theism-*disfavoring* evidence (suffering/evil per Draper, divine hiddenness, the biological non-necessity of pain-as-signal, etc.) into the same running product. Swinburne does address evil and hiddenness but assigns them low disconfirming weight; Draper and others argue this weighting is unmotivated and the correct combined calculation nets negative, i.e., cumulative reasoning is symmetric machinery that doesn't intrinsically favor theism — it just favors whichever side does the more careful (or more motivated) evidence-selection and weighting.
4. **Ill-defined likelihoods (Sober/Philipse point, generalized).** The entire multiplication is only meaningful if each P(Eᵢ|theism) is a real, non-arbitrary number. If (as Sober argues for design-type evidence, and Philipse argues for theism generally) you can't fix a designer's goals/abilities or theism's predictive content independently of the very evidence you're trying to explain, then each term in the product is stipulated rather than derived — cumulative "confirmation" becomes an artifact of how generously each likelihood was chosen, not a real accumulation of evidential force.

**Bottom line on cumulative cases:** the mathematics of independent-evidence multiplication is sound and uncontroversial in general (it's the same math behind combining independent diagnostic tests in medicine). The controversy is entirely about whether theistic cumulative cases satisfy the preconditions (true independence, well-defined non-arbitrary likelihoods, symmetric inclusion of disconfirming evidence, and a defensible starting prior) — and the specialist critical literature (Sobel, Philipse, Draper, Sober) converges on "no, not as usually run," while Swinburne and other theist Bayesians maintain the preconditions are adequately met. This is an active, unresolved dispute among people who agree on the formal apparatus — it is not a case of one side not understanding Bayes.

## 5. Honest bottom line

**What a well-calibrated person can say:**
- Professional philosophers, as a population, lean atheist by a wide and stable margin (~67% vs ~19%, both 2009 and 2020) — this is a real, well-documented data point, and it is *some* evidence, in the weak "appeal to relevant expert consensus" sense, though philosophy is unlike physics in that there is far less consensus-generating mechanism (no experiments settle metaphysics) — so the evidential weight of this consensus is lower than, say, physicist consensus on relativity.
- The 78%-theist figure among philosophy-of-religion specialists is real but is substantially compromised as *independent* evidence for theism by a plausible, argued (Draper & Nichols) selection-effect story: people self-select into the subfield partly because they already hold or want to defend theistic commitments, and the subfield's institutional history (many programs seeded via religiously-affiliated universities/seminaries) reinforces this. This doesn't make PoR specialists' *arguments* wrong — but it means "78% of the specialists agree" should not be read the way you'd read "97% of climatologists agree," because the selection mechanisms into the two fields are structurally different (one selects on prior commitment to the conclusion, the other doesn't).
- The Bayesian program (Swinburne et al.) is formally legitimate — Bayes' theorem is not the weak point — but every serious application to "does God exist" runs aground on the same three unresolved problems: (a) no non-arbitrary way to fix a prior for a metaphysically maximal, non-repeatable hypothesis like theism (there's no reference class to draw a base rate from), (b) contested and possibly incoherent content for what "God" even predicts (Philipse, Sober), and (c) unresolved independence/weighting issues in combining multiple lines of evidence. Both Swinburne's ~0.5+ and various atheist Bayesians' near-zero results come from defensible-looking math built on contestable, non-empirically-fixed inputs — the calculations are not wrong, the inputs are disputed, and there's no agreed procedure for arbitrating the dispute. This is a case where "do the Bayesian math" doesn't resolve the disagreement, because the disagreement is precisely about what numbers to plug in.
- **What "evidence for God" even means is itself part of the dispute.** Fine-tuning, consciousness, religious experience, and moral order are all data that *both* naturalists and theists must explain — they aren't theism-exclusive facts. Whether they count as "evidence for God" depends on a prior judgment about how much explanatory credit a hypothesis gets for *entailing* observed facts vs. how much it's penalized for *low prior plausibility given its enormous ontological commitment* (an infinite, omniscient, omnipotent, freely-willing immaterial mind) — reasonable, informed people disagree on how to trade these off, and there's no neutral, non-question-begging way to settle which trade-off is "correct." This is not primarily a factual disagreement; it is partly a disagreement about epistemic method.
- **The bare-theism/specific-religion gap is large and frequently elided.** Even a fully successful Bayesian cumulative case in the style of Swinburne would, at best, argue for a generic, philosophically thin theism — a single, simple, omni-property first cause / ground of being (closer to classical deism or Plotinian "the One" than to any specific creed). Getting from that bare theism to a *specific* historical religion's God (Trinitarian, incarnate, resurrected, textually self-revealing, morally commanding in specific ways) requires an entirely separate, additional evidential case — historical/testimonial arguments about scripture, miracles, and specific revelation claims (this is exactly why Swinburne writes *The Existence of God* and then a *separate* book, *The Resurrection of God Incarnate*, to make that second jump; the "97%" figure people quote comes from the second book, not the first). The two arguments have different evidence bases, different failure modes, and very different levels of scrutiny in the literature — the jump from "a first cause/ground of being plausibly exists" to "therefore my specific tradition's God, with its specific doctrines, is true" is the single most commonly skipped step in popular God-arguments, and it is *not* covered by fine-tuning, cosmological, or ontological arguments at all — those only ever target bare theism.

**What a well-calibrated person cannot say:**
- Cannot say "professional consensus settles this" in either direction — philosophy has no analogue of experimental confirmation to generate the kind of consensus that would make expert opinion strongly diagnostic, and the one subfield with the strongest pro-theism consensus (PoR) has a live, specific, published selection-effect explanation for that consensus that the specialists themselves (Draper is a philosopher of religion) take seriously.
- Cannot say Swinburne's "97%" (or any single precise numeric probability, from either side) is a rigorously derived figure rather than a Bayesian-notation dressing on ultimately intuitive/contested prior and likelihood judgments — this critique is near-universal even among philosophers sympathetic to natural theology.
- Cannot treat "cumulative case" as automatically strong just because it's phrased in Bayesian terms — the accumulation is only as good as its independence assumptions and the honesty/symmetry of which evidence gets included, both of which are exactly where the live disputes sit.
- Cannot collapse "is there a first cause / ground of being" and "is [specific religion]'s God real" into one question — they require different arguments and different evidence, and most popular apologetics (and popular atheist rebuttals) conflate the two.

---
**Inference flags used above:** the "symmetry" counter-consideration about analytic philosophy's own possible naturalism-selection bias (§2) is my own reasoned addition, not sourced to a specific paper — everything else is attributed to a specific named source above.
