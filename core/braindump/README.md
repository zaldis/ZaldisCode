# Braindump

The goal of this CLI tool is to aggregate personal notes from multiple `*.md` files into a single knowledge.txt file.
This consolidation enables AI agents, such as NotebookLM, to analyze your existing knowledge base, identify gaps,
and suggest areas that require further research or dedicated resources.

## Prompt to extract new knowledge from the resource

```
**Context**:
I have uploaded two primary sources: knowledge.txt (my current expertise) and {resource} (the new material).

**Objective**:
Perform a comparative gap analysis. Identify information in {resource} that is either entirely absent from knowledge.txt
or provides a significantly deeper level of detail than what I currently have recorded.

**Output Format**:
Please provide a detailed overview organized by the following categories:

* New Knowledge Frontiers:
  Identify specific concepts, theories, or data points in {resource} that do not appear in knowledge.txt.
* Strategic Application:
  For each new piece of knowledge, explain a practical use case or how it shifts the perspective of my existing notes.
* Source Mapping:
  Explicitly state the chapter and page numbers (or section headers) in {resource} where this information is located.
* Integration Synthesis:
  Describe how this new information "plugs into" my current knowledge base.
  Does it contradict a previous note, expand on a basic concept, or provide a missing link between two existing topics?
```
