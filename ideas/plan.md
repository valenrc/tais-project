# Plan : Multilingual Personality Shift — Mechanistic Interpretability
(generado con Claude Opus 4.6 (skill /brainstorm))

## Metadata

- **Proyecto**: Multilingual Personality Shift
- **Campo**: Multilingual Safety × Mechanistic Interpretability
- **Duración**: 5 semanas / 30 horas totales
- **Entregable final**: Blog post publicado con 1-3 claims concretos
- **Cómputo**: GPU vía RunPod (A6000 48GB o A100 40GB, ~$20-40 total estimado)
- **Modelo principal**: Qwen2.5-7B-Instruct (soporte fuerte EN/ZH, validado en papers base)
- **APIs**: Gemini Pro o GPT-4.1-mini como juez evaluador
- **Herramientas**: Git/GitHub, uv, Claude Code + skills, safety-tooling, RunPod

## Pregunta de investigación

**¿Los vectores de persona extraídos en inglés son válidos para monitorear y controlar rasgos de personalidad cuando el modelo opera en distintos idiomas (español, chino, y algún otro idioma que esté escasamente representado en el dataset)?**

### Claims candidatos para el blog post (elegir 1-3)

1. Los persona vectors para el rasgo X son [universales / language-specific] entre EN, ZH y ES, con cosine similarity de Y.
2. El steering cross-lingual con vectores extraídos en inglés [funciona / no funciona] cuando el modelo genera en otros idiomas.
3. El Assistant Axis es [igualmente estable / menos estable] en conversaciones en ZH/ES que en EN.

## Narrativa: conexión entre los 4 papers citados

1. **Schut et al. (2025)** — Los LLMs "piensan en inglés": representaciones internas pasan por un espacio cercano al inglés. English steering vectors son más efectivos que los nativos.
2. **Chen et al. (2025)** — Los rasgos de personalidad (evil, sycophancy, hallucination) se codifican como direcciones lineales en el espacio de activaciones: *persona vectors*.
3. **Lu et al. (2026)** — PCA sobre el espacio de personas revela un "Assistant Axis" (PC1). Alejarse de este eje predice drift hacia comportamientos dañinos. Activation capping reduce jailbreak success ~60%.
4. **Wang et al. (2025)** — La dirección de rechazo (refusal) es universal entre idiomas alineados, pero diverge en idiomas de bajos recursos.

**Propuesta (a revisar con novelty-check)**: Nadie ha estudiado si los persona vectors (no solo refusal) se transfieren entre idiomas. El refusal vector es universal, pero ¿el evil vector lo es? ¿El Assistant Axis es igualmente estable en ZH/ES?

## Cronograma alineado al curso (5 semanas, 30 horas)

### Semana 1 — Setup y replicación en inglés (~8h)

**Entregable**: Proyecto elegido, pregunta de investigación definida, pipeline funcionando en EN.

**Hipótesis a testear**: "Puedo reproducir la extracción de persona vectors en inglés y obtener resultados consistentes con el paper original."

**Qué me haría cambiar de opinión**: Si el pipeline no corre o los resultados divergen mucho del paper, debo entender por qué antes de avanzar.

Tareas:
- [ ] Clonar repos `safety-research/persona_vectors` y `safety-research/assistant-axis`
- [x] Configurar entorno (Vertex AI Workbench, NVIDIA L4)
- [x] Replicar extracción de persona vectors para **un solo rasgo** (evil) en inglés en Qwen2.5-7B-Instruct → `experiments/week1/persona_vectors_replication.ipynb`
- [x] Validar: ¿el vector extraído produce steering efectivo? (steering + monitoring en el notebook)
- [ ] Documentar setup en research log
- [ ] Iniciar repo en GitHub

**Principio guía**: *Empezá con el experimento más simple posible.* Un rasgo, un idioma, verificar que funciona.

### Semana 2 — Extensión multilingüe: primer resultado (~8h)

**Entregable**: Primeros resultados comparando persona vectors EN vs ZH (y opcionalmente ES).

**Hipótesis a testear**: "Los persona vectors para 'evil' extraídos en chino serán similares a los extraídos en inglés (cosine similarity > 0.5), dado que el modelo 'piensa en inglés' (Schut et al.)."

**Qué me haría cambiar de opinión**: Cosine similarity muy baja (<0.3) sugeriría que la personalidad es language-specific, no universal.

Tareas:
- [ ] Adaptar el pipeline para generar prompts contrastivos en chino simplificado
  - Modificar los prompts de generación de artefactos para que el LLM genere en ZH
  - Verificar manualmente la calidad (ventaja: trilingüismo nativo)
- [ ] Extraer persona vector para evil en ZH
- [ ] **Primer resultado clave**: cosine similarity entre evil_EN y evil_ZH por capa
- [ ] Si hay tiempo: repetir para ES y/o un segundo rasgo (sycophancy)
- [ ] Visualización rápida: heatmap de cosine similarity por capa

**Baseline**: Comparar cosine similarity de persona vectors cross-lingual con la de refusal vectors cross-lingual (Wang et al., 2025). ¿Son igual de universales?

### Semana 3 — Steering cross-lingual + outline del blog (~8h)

**Entregable**: Outline del blog post con hallazgos principales. Resultados de steering.

**Hipótesis a testear**: "Aplicar el evil vector extraído en inglés durante generación en chino produce un efecto comparable al evil vector nativo en chino."

**Qué me haría cambiar de opinión**: Si el steering en EN no tiene efecto en ZH, o produce un efecto cualitativamente diferente.

Tareas:
- [ ] **Steering cross-lingual**: aplicar evil vector EN durante generación en ZH/ES. Evaluar con juez LLM
- [ ] **PCA**: si extraje ≥2 rasgos × ≥2 idiomas, hacer PCA conjunto y visualizar clustering
- [ ] Opcional: extraer Assistant Axis en ZH, comparar con EN
- [ ] Red-teamear resultados:
  - ¿Podría el cosine similarity alto ser un artefacto del tokenizer compartido?
  - ¿Hay una explicación más simple (e.g., las preguntas de evaluación son demasiado similares entre idiomas)?
- [ ] **Escribir outline del blog post** con claims provisorios y figuras clave

### Semana 4 — Consolidación y blog post (~4h)

**Entregable**: Blog post publicado.

Tareas:
- [ ] Correr experimentos adicionales si hay gaps en la evidencia
- [ ] Producir figuras finales (PCA, heatmaps, steering comparison)
- [ ] Escribir blog post: 1-3 claims concretos, con evidencia y limitaciones honestas
- [ ] Discutir limitaciones:
  - Solo 1 modelo (Qwen2.5-7B)
  - Solo 2-3 idiomas
  - Solo 1-3 rasgos
  - 30 horas de dedicación total

### Semana 5 — Presentación (~2h)

**Entregable**: Presentación / demo del proyecto.

- [ ] Preparar presentación con las figuras clave
- [ ] Opcional: demo interactiva de steering cross-lingual

## Estrategia de scoping: empezá simple, escalá

El proyecto tiene muchas dimensiones que se pueden expandir. La estrategia es empezar con la versión mínima y escalar según el tiempo disponible:

| Prioridad | Dimensión | Mínimo viable | Expansión si hay tiempo |
|---|---|---|---|
| 1 | Rasgos | Evil solamente | + sycophancy, + hallucination |
| 2 | Idiomas | EN vs ZH | + ES, + idioma de bajos recursos |
| 3 | Análisis | Cosine similarity por capa | + PCA, + CCA/SVCCA |
| 4 | Intervenciones | Steering cross-lingual | + activation capping, + probing |
| 5 | Modelos | Qwen2.5-7B | + Llama-3.1-8B |

**El proyecto mínimo viable es**: extraer evil vector en EN y ZH, medir cosine similarity, testear steering cross-lingual. Eso ya es un blog post publicable.

## Baselines (invertí esfuerzo real acá)

1. **Random baseline**: cosine similarity entre un vector aleatorio y un persona vector. ¿Es significativamente menor que la similarity cross-lingual?
2. **Refusal vector baseline**: replicar la extracción de refusal direction (Wang et al., 2025) en EN y ZH con el mismo modelo. ¿Los persona vectors son más o menos universales que el refusal vector?
3. **Rasgo cruzado**: cosine similarity entre evil_EN y sycophancy_ZH. Debería ser baja si los vectores realmente capturan rasgos distintos.

## Red-teaming: preguntas difíciles para hacerme a mí mismo

- ¿Podría la alta cosine similarity ser un artefacto del tokenizer multilingüe compartido?
- ¿Estoy comparando las mismas capas? ¿La información de personalidad podría estar en capas diferentes según el idioma?
- ¿Los prompts contrastivos en chino son realmente equivalentes a los de inglés, o introducen sesgos culturales?
- ¿El juez LLM evalúa con el mismo estándar en todos los idiomas?
- ¿Hay una explicación trivial tipo "el modelo traduce internamente a inglés y por eso los vectores son iguales"? (si es así, ¿qué implicaciones tiene para safety?)

## Herramientas y código existente

| Recurso | URL |
|---|---|
| Persona Vectors (código) | https://github.com/safety-research/persona_vectors |
| Assistant Axis (código) | https://github.com/safety-research/assistant-axis |
| safety-tooling | https://github.com/safety-research/safety-tooling |
| Vectores pre-computados | HuggingFace: `lu-christina/assistant-axis-vectors` |
| Paper Persona Vectors | https://arxiv.org/abs/2507.21509 |
| Paper Assistant Axis | https://arxiv.org/abs/2601.10387 |
| Paper Refusal Direction | https://arxiv.org/abs/2505.17306 |
| Paper Multilingual Think English | https://arxiv.org/abs/2502.15603 |

## Papers adicionales relevantes

- **PERSONA (ICLR 2026)**: Álgebra vectorial sobre persona vectors (composición, intensidad). arXiv:2602.15669
- **Cross-Lingual Activation Steering (2026)**: Steering multilingüe training-free. arXiv:2601.16390
- **Language Vectors (2026)**: Steering con vectores de idioma para multilingual ICL. arXiv:2602.02326
- **Multilingual Safety via Sparse Weight Editing (2026)**: Transferencia de safety EN→LRL vía transformación de representaciones. arXiv:2602.22554
- **Shared Safety Neurons (2026)**: Neuronas de seguridad compartidas cross-lingual (<0.3% del modelo). arXiv:2602.01283

## Resultado esperado

Un blog post con 1-3 claims concretos sobre la universalidad (o no) de los persona vectors entre idiomas, con evidencia cuantitativa (cosine similarity, PCA, steering experiments) y limitaciones honestas.

**Ejemplo de título de blog post**: *"Do Persona Vectors Speak Other Languages? Cross-Lingual Transfer of Personality Traits in LLMs"*

## Riesgos y mitigaciones

| Riesgo | Mitigación | Señal de alerta |
|---|---|---|
| Pipeline no corre / setup toma demasiado | Pedir ayuda a facilitadores inmediatamente. El código está bien documentaado | Si al final de semana 1 no tengo un vector extraído, escalar |
| Los vectores son idénticos entre idiomas | Es informativo: confirma universalidad. Agregar un idioma de bajos recursos para buscar divergencia | Cosine similarity > 0.95 en todas las capas |
| Los vectores son totalmente diferentes | También informativo: la personalidad es language-specific. Probar steering cross-lingual para ver si aún así funciona | Cosine similarity < 0.1 |
| No hay acceso a GPU | Pivotar a Plan B (black-box vía APIs) | Si RunPod no está disponible para semana 1 |
| 30 horas no alcanzan | Mantener scope mínimo: 1 rasgo × 2 idiomas. El blog post puede reportar resultados parciales + trabajo futuro | Si al final de semana 2 no tengo primer resultado |
| Qwen2.5-7B tiene calidad baja en ES | Priorizar EN vs ZH (donde Qwen es fuerte). ES es extensión opcional | Respuestas incoherentes en español |

## Ventajas competitivas

- **Trilingüismo nativo** (español, chino, inglés): verificar calidad de prompts sin depender de MT
- **Experiencia con PCA/LSI**: familiaridad con reducción de dimensionalidad
- **Resultados preliminares**: experimentos con roleplay jailbreaks en Gemini
- **Código existente**: ambos repos (persona_vectors, assistant-axis) están bien documentados y listos para usar

## Fail fast checklist

Preguntarme al final de cada semana:

- [ ] ¿Estoy aprendiendo algo sobre el problema?
- [ ] ¿Tengo al menos un resultado concreto (número, figura, observación)?
- [ ] ¿Puedo explicar en una oración lo que descubrí esta semana?
- [ ] ¿Mi research log está actualizado?
- [ ] ¿Necesito pivotar o puedo seguir en esta dirección?
