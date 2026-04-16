# Meiji Letter Lexicon

## Overview

This repository contains a structured lexicon of interpretive terms extracted from Meiji-era correspondence.

The dataset is designed to support the interpretation of historical documents and to enable corpus construction and computational analysis of historical semantics.

Each entry represents a context-dependent interpretation of expressions found in historical letters.

This dataset can be used as:
- A lexicon of historical euphemisms and their interpretations
- Training data for classification tasks (event types, named entities)
- A resource for semantic analysis of political language

---

## Data Structure

The dataset is provided in JSON format.

Each record includes the following fields:

* `case_id`
  Unique identifier for each entry.

* `letter_id`
  Identifier of the original letter.

* `date`
  Date of the letter (Japanese era format).

* `expression`
  The original expression found in the letter.

* `interpretation`
  Interpreted meaning of the expression based on context.

* `excerpt`
  Excerpt from the original text where the expression appears.

* `event_type`
  Type of event or situation.
  Typical examples of `event_type` include:

Typical values of `event_type` include:

* `title（肩書）` — official titles or positions (e.g., government posts, ranks)
* `organization（機関名）` — institutions, organizations, or administrative bodies
* `object（事物）` — material objects, goods, or concrete items
* `person（人物）` — references to individuals
* `building（建物）` — buildings, residences, or facilities
* `place（地名）` — geographical locations
* `term（用語）` — abstract terms, concepts, or expressions
* `movement（動静）` — actions related to movement, travel, or changes in location

These categories reflect the current data structure and may be refined in future versions.
Note that these categories are heuristic and may be refined in future versions.

* `persons`
  Related individuals mentioned in the context.

* `places`
  Related locations.

* `source_1`, `source_2`
  Source information of the letter.

* `note` (optional)
  Additional remarks or contextual notes.

* `basis` (optional)
  Explanation of how the interpretation was derived.

* `contributor` (optional)
  Name of the person who created the entry.

* `status` (optional)
  Interpretation status (e.g., "confirmed", "tentative").

Missing values are represented as `null`.

---

### Source Material

All data in this dataset were created based on the following source:

- *Shinagawa Yajiro Kankei Monjo 8* (尚友倶楽部品川弥二郎関係文書編纂委員会編『品川弥二郎関係文書8』山川出版社、2017年),  
  ISBN: 978-4-634-51080-7

The dataset does not include the original texts themselves, but only structured metadata extracted from them.

---

## Data Creation Policy

* One row corresponds to one interpretive case.
* Multiple entries may be extracted from a single letter.
* Interpretations are context-dependent and may vary depending on available information.
* When necessary, interpretations may incorporate:

  * Envelope information
  * Related historical documents
  * Known relationships between individuals

---

## Input Guidelines

* `letter_id` is constructed as a composite identifier.
  "YS" refers to the *Shinagawa Yajirō Related Documents*,
  the number (e.g., "8") indicates the volume,
  and the remaining part (e.g., "AY85") represents the sender and document number.
  For example, "YS8AY85" refers to document no. 85 sent by Yamagata Aritomo in volume 8 of the *Shinagawa Yajirō Related Documents*.

* Each entry in `expression` (including euphemistic or indirect expressions) must correspond to a single item per row.
  If multiple relevant expressions or names appear in the same sentence, they should be recorded as separate entries.

* The `excerpt` field must contain the full sentence in which the expression appears, copied as-is from the original text.

* The `persons` field should include not only individuals explicitly mentioned in the sentence, but also all individuals relevant to the interpretive context of the entry.

* The `source_1` field records sender and recipient information of the letter, formatted as "sender → recipient".

* The `source_2` field records the source collection or archival group of the letter.
  In the current version, all entries are recorded as "Shinagawa Documents, vol. 8".

---

## Interpretation Policy

The interpretations in this dataset are not always definitive.

Some entries are based on:

* indirect evidence,
* contextual inference,
* or partial information.

These cases may be marked using the `status` field or described in the `note` / `basis` fields.

---

## Notes on Omitted Information

In the original data collection template, a "remarks" field included various types of information such as:

* reasoning behind interpretations,
* responsibility of contributors,
* and notes for future verification.

In this initial release, such information has been partially omitted or simplified.

Future versions may reintroduce this information in a more structured format.

---

## Contributors

This dataset was created by students as part of the Modern Japanese History Seminar course at Kyoto Prefectural University, through a research-oriented data collection and interpretation project.

Supervision and project design were conducted by the repository owner.

Individual contributors may be recorded within each entry.

---

## Intended Use

This dataset is intended for:

* interpretation of historical correspondence
* corpus construction
* semantic analysis of historical language
* integration with NLP workflows

---

## License

This dataset is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

---

## Future Development

Planned improvements include:

* expansion of the dataset
* refinement of interpretation categories
* inclusion of structured reasoning and metadata
* integration with larger historical corpora
