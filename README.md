# Amazon Image Design Skill

Amazon Image Design Skill is a Codex skill for planning, analyzing, generating, and reviewing Amazon listing images and ecommerce product visuals.

It is designed for Amazon operators, designers, and sellers who need marketplace-aware image plans, competitor-informed creative direction, and strict product fidelity when turning product materials into listing images.

## What It Does

- Creates Amazon image design plans for main images, lifestyle images, infographics, comparison images, size charts, package images, A+ visuals, and ecommerce gallery sets.
- Uses market and competitor research when product categories, reference images, Amazon links, reviews, Q&A, or competitor pages are provided.
- Keeps every image focused on one clear visual message instead of piling up selling points.
- Prioritizes scene-based, immersive ecommerce design where appropriate.
- Applies Amazon image compliance baselines for main images and secondary listing images.
- Enforces strict product fidelity: the product shape, color, labels, text, proportions, materials, and functional details must match the user's source image.

## Default Output Standards

For the user's Amazon design workflow, the skill uses these defaults:

- Square images: `2000 x 2000 px`
- Vertical 4:5 images: `1600 x 2000 px`
- Other ratios: longest side at least `2000 px`
- Main image: pure white background, product only, no overlays, no props unless included
- Secondary images: lifestyle scenes, concise callouts, size charts, comparison, detail close-ups, and usage steps when truthful and useful

The skill treats outputs below 2K quality as unsuitable unless a smaller derivative is explicitly requested.

## Product Fidelity Rules

Product fidelity is the most important rule in this skill.

When a user provides a product image, the product is treated as the locked source of truth:

- Do not deform the product.
- Do not change its color.
- Do not change visible text, labels, logos, ports, seams, stitching, buttons, or functional details.
- Do not invent accessories or included parts.
- Do not change the product function.
- Do not resize the product in a way that makes the scene unrealistic.

If a generated or edited image changes the product's actual appearance, the result is considered unusable and must be revised.

## Repository Structure

```text
amazon-image-design-skill/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
└── references/
    └── amazon-image-requirements.md
```

## Installation

Copy the `amazon-image-design` skill folder into your Codex skills directory:

```powershell
Copy-Item -Recurse -Force . "$env:USERPROFILE\.codex\skills\amazon-image-design"
```

Then restart Codex so the skill can be discovered.

## Typical Use

Example prompts:

```text
Use amazon-image-design to create a 7-image Amazon gallery plan for this product.
```

```text
Analyze these competitor links and design a 1600x2000 lifestyle image for my product.
```

```text
Create a 2000x2000 Amazon main image. Keep the product exactly the same as the source photo.
```

```text
Generate a scene-based infographic image with one primary selling point and minimal copy.
```

## Workflow

The skill follows this process:

1. Confirm the product, marketplace context, image role, ratio, source materials, and any must-use copy.
2. Review Amazon image requirements when upload readiness or main-image compliance matters.
3. Research competitor pages, reference links, reviews, Q&A, and category patterns when available.
4. Propose an original image direction with composition, copy, color, typography, product placement, and compliance notes.
5. Generate or edit the image when requested.
6. Run a quality gate for dimensions, product fidelity, text legibility, visual hierarchy, claim safety, and Amazon compliance.

## Amazon Compliance Reference

The included reference file captures baseline Amazon image requirements and local workspace defaults:

- Pure white main-image background: RGB `255, 255, 255`
- Actual product shown clearly
- Product should fill about 85% or more of the main-image frame
- No badges, borders, watermarks, rating graphics, text overlays, or promotional graphics on main images
- Accepted formats commonly include JPG/JPEG, PNG, and TIFF
- At least 1000 px on the longest side for zoom eligibility
- Category-specific rules may add extra restrictions

For final upload-critical work, verify current Seller Central and category-specific guidance because Amazon requirements and enforcement can change.

## Notes

This skill is intentionally practical rather than theoretical. It is meant to support real Amazon image production: strong commercial judgment, clean visual hierarchy, market-aware design, and hard checks before calling an image usable.
