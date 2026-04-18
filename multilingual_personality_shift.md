# 9: Multilingual personality shift
ID: x Research Field: Multilingual Safety

Scores: theory_of_impact: x| accessible_complexity: x | narrow_scope: x | novelty: x (confidence: x) Novelty: x) | Weighted Score: x

Research Question: Personality of LLMs determines safety. Non-english safety is consistently worse in most open LLMs. It is very likely that english post-training safety can be translated to other languages.
How does the personality geometry or landscape shift under different languages? Can we come up with causal interventions to translate english safety to other languages?

Approach: Extract persona vectors in different languages. Compare them head-to-head. Run basic PCA to reduce dimensionality. Use canonical correlation analysis to remove rotational variance. Identify “Assistant Axis”. Try mechanistic (steering, probing, patching) or black-box (prompting, scaffolding) methods to improve safety in other languages without additional training data.

Strength Rationale:

Safety is bottlenecked by the amount of training data for a given language. Low-resourced languages are unsafer. Another constraint is the amount of post-training (RLHF, etc.). If we find ways to generalize safety training across languages we skip these limitations.

Cited Sources:

Schut, Lisa, Yarin Gal, and Sebastian Farquhar. ["Do multilingual llms think in english?." (2025)](https://arxiv.org/abs/2502.15603).
Chen, Runjin, et al. ["Persona vectors: Monitoring and controlling character traits in language models." (2025).](https://arxiv.org/abs/2507.21509)
Wang, Xinpeng, et al. ["Refusal direction is universal across safety-aligned languages." (2025).](https://arxiv.org/abs/2505.17306)
Lu, Christina, et al. ["The assistant axis: Situating and stabilizing the default persona of language models." (2026).](https://arxiv.org/abs/2601.10387)