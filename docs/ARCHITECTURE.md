# Proof Loom architecture

## Product boundary

The Proof Loom is an explanatory, deterministic visualization of public claims. It does not execute, certify, or continuously monitor the featured repositories. Every simulated challenge is labelled as such.

## Runtime

The public experience is dependency-free static HTML, CSS, and JavaScript. It loads one local JSON manifest, renders the loom with Canvas 2D, and preserves a semantic HTML project index. This keeps deployment auditable and avoids third-party runtime failure.

## Information flow

```text
public claims + boundaries
        ↓
docs/data/evidence.json
        ↓
validation and deterministic README rendering
        ↓
interactive canvas + semantic direct index
        ↓
repository, product, and reproduction links
```

## Interaction model

- Horizontal pointer movement controls the shuttle.
- Vertical position selects a project strand.
- Keyboard: arrows operate the shuttle and strand selection; Enter opens evidence; C applies the first controlled challenge.
- Challenge toggles affect only the explanatory visual model.
- The evidence drawer exposes canonical evidence and limitations.

## Determinism

Strand disturbances are seeded from each documented commit string. The same manifest and implementation produce the same base strand geometry.

## Failure behavior

- If Canvas is unavailable, the direct index remains usable.
- If JavaScript is unavailable, the document landmarks and explanatory copy remain visible; README contains the canonical first-contact story.
- If the evidence manifest cannot load, the canvas reports failure and visitors retain direct GitHub links.
- No API call is required at runtime.

## Future WebGPU path

A later version may add GPU-deformed fibre geometry, but it must remain progressive enhancement. The semantic project index, reduced-motion mode, and direct evidence paths are canonical.
