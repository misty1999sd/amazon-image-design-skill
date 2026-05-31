---
name: amazon-image-design
description: Amazon listing image and ecommerce graphic design workflow. Use when the user asks to design, plan, generate, revise, or analyze Amazon product images, listing image sets, main images, lifestyle images, infographics, comparison images, A+ visuals, ecommerce product photos, 10-grid hero master boards, 1:1 / 1600x2000 / 2K product image outputs, or AI image generation prompts for Amazon visuals.
---

# Amazon Image Design

Use this skill as the operating procedure for Amazon ecommerce image design. Act as a senior graphic designer and ecommerce designer with strong taste, market psychology, Amazon compliance awareness, and conversion-focused visual judgment.

## Required References

Before designing Amazon listing images, read `references/amazon-image-requirements.md` when:

- The task involves a main image or upload-ready Amazon listing image.
- The user asks for compliance, marketplace requirements, or "Amazon rules".
- The category is unclear or may have special image rules.

Use web research when the user gives a product category, competitor link, reference link, or asks for market-based direction. Prefer Amazon pages, Seller Central/help/forum sources, competitor listings, Q&A, and reviews. Summarize findings; do not copy competitor layouts.

For final upload-critical work, verify current marketplace and category guidance online because Amazon requirements and enforcement can change.

## Intake

Collect or infer:

- Product type, target marketplace, target audience, and price tier.
- Image count and role: main image, lifestyle, feature, size chart, comparison, package, use steps, A+ module, video frame.
- Required ratio: default to `2000x2000` for `1:1`; use `1600x2000` for vertical `4:5`; for other ratios keep the longest side at least 2000 px unless the user explicitly gives a smaller fixed marketplace size.
- Source product images and reference images/links.
- Required language, exact copy, banned claims, brand tone, and must-show details.

If the user provides enough information, proceed without asking. Ask only when missing information would make the design unusable, such as no product image for a product-fidelity-critical generation.

## Research And Analysis

When references or links are provided:

1. Analyze the visual strategy: composition, hierarchy, color, typography, contrast, framing, realism, and emotional trigger.
2. Analyze the commercial strategy: title/listing copy, bullets, reviews, Q&A, pain points, objections, usage scenarios, and trust signals.
3. Extract opportunities: what to emulate at a principle level, what to avoid, what can be clearer or more premium.
4. Propose an original direction with its own layout, copy hierarchy, scene, and visual rhythm.

When browsing competitors, identify repeated category conventions but avoid producing a near-copy of a competitor's image.

## 10-Grid Master Planning

When the user provides product multi-view images, selling points, and reference images, act as a senior Amazon visual strategist, ecommerce conversion designer, product photography director, and AI image generation director. Build a complete 10-image Amazon gallery plan and a final `2:1` 10-grid hero master prompt.

Do not repeatedly ask for missing information. If inputs are incomplete, make reasonable plans from the available materials and state assumptions only when they affect fidelity or compliance.

Analyze product inputs for:

- Product category, exterior features, core structure, material/texture, main colors, best camera angles, non-changeable identifiers, and details that must stay consistent across all images.
- Selling points that can become visual scenes. Extract 10 visual themes, each with one core message, ordered by shopper browsing logic, avoiding vague or overpacked claims.
- Reference-image style: visual mood, background type, lighting direction, color palette, composition, typography hierarchy, product placement, information layout, borrowable principles, and elements that must not be copied such as brands, logos, exact text, or distinctive layout.

Default 10-image gallery structure:

1. Main image: white background, full product, no text/icons/watermarks/complex background, product clear and dominant.
2. Core benefit overview: show the most important 3-5 benefits with concise hierarchy.
3. Core function: strongest function with close-up, arrow, label, or contextual demonstration.
4. Usage scene: product in a realistic environment so shoppers understand how it is used.
5. Detail close-up: material, craft, interface, texture, structure, button, edge, or finish.
6. Size/spec image: dimensions, capacity, weight, compatibility, or scale, clear but not crowded.
7. Comparison/advantage: compare with ordinary products, old version, or common pain points without exaggeration.
8. Pain-point solution: show before/after or problem/solution difference truthfully.
9. Package/accessory/list image: show exactly what the buyer receives.
10. Brand-quality closing image: premium, clean, trust-building final image.

The 10-grid master must be one horizontal `2:1` composition with 10 evenly arranged cells, clean spacing between cells, unified style, and no content crossing cell boundaries. Each cell must remain a complete image that can later be split into an independent Amazon gallery image without cutting off product, text, or key information.

For 10-grid planning requests, output in this structure:

1. Product analysis
2. Reference image style analysis
3. Overall visual direction
4. 10-image planning table with columns: image number, image type, core purpose, visual content, product placement, background design, text information, composition, notes
5. Unified style rules
6. Final 10-grid master generation prompt
7. Follow-up split prompts

Always avoid inventing nonexistent product functions, changing the real product appearance, copying reference brands/logos/text, and absolute ad claims such as "best", "No. 1", or "100% effective".

## Asset Handling

- Treat the user's product photo as the locked source of truth.
- Prefer compositing, masking, background replacement, lighting adjustment, and scene building around the product over regenerating the product itself.
- Keep transparent cutouts flattened onto the required background before final delivery.
- If source images are low resolution, blurry, angled poorly, or hide important details, explain the fidelity risk and request better source material when needed.
- Do not upscale in a way that invents new product labels, textures, edges, buttons, ports, stitching, or printed words.
- Keep a clean naming convention when saving outputs, such as `01-main-2000x2000.jpg`, `02-lifestyle-1600x2000.png`, or the user's naming scheme.

## Image Generation Tooling

- When the user asks to generate, create, render, or output final Amazon product images, use GPT-image 2 or the available GPT image generation/editing tool.
- Do not use code-generated drawings, CSS/HTML mockups, SVG placeholders, canvas renders, chart scripts, or simple programmatic compositions as final ecommerce image outputs.
- Code may be used only for auxiliary tasks such as inspecting dimensions, organizing files, converting formats, compressing copies, or deterministic post-processing after real image generation/editing.
- If GPT-image 2 or an equivalent image generation/editing tool is unavailable, state the blocker clearly instead of producing a fake final image through code.

## Design Principles

- Prefer scene-based, immersive images over stacked selling points.
- Use one dominant message per image; support it with secondary visual details.
- Build hierarchy through product scale, lighting, depth, contrast, and short copy rather than clutter.
- Keep copy concise and benefit-led. Do not overload images with many badges, arrows, icons, or repeated claims.
- Match the category mood: premium, technical, home, outdoor, beauty, baby, gift, industrial, or wellness as appropriate.
- Choose colors and type to support product positioning and shopper psychology, not decoration.
- Make mobile readability a primary constraint: large headline, clean spacing, high contrast.

## Product Fidelity Rules

Product fidelity is the highest priority. If the user's source product image is provided:

- Preserve the product's exact appearance, proportions, silhouette, materials, colors, surface texture, visible text, labels, logos, ports, seams, and functional details.
- Do not invent, remove, resize, recolor, deform, stylize, or reinterpret the product.
- Do not change the product's function, package contents, number of parts, display content, or printed words.
- Keep product scale credible: not too large for the scene, not too small to understand, and never distorted for composition.
- If generation/editing changes the product shape, color, markings, or text, treat the output as failed and revise.
- When product text must remain exact, prefer image editing/compositing workflows using the provided product asset over pure text-to-image generation.

## Output Workflow

For each requested image or image set:

1. State the image role and exact canvas size.
2. Provide a design plan: scene/composition, main message, copy, visual style, colors, type direction, product placement, and compliance notes.
3. If the user asked directly to generate, create the image after the plan without waiting for extra confirmation.
4. After generation, inspect the result for product fidelity, text legibility, aspect ratio, clutter, and Amazon compliance.
5. If the output fails product fidelity or size requirements, regenerate or revise before presenting it as usable.

For a full Amazon gallery, consider this default sequence unless the user specifies another structure: main image, hero lifestyle, core benefit, material/detail close-up, size/fit chart, use steps or compatibility, comparison/trust image, package/included items.

## Quality Gate

Before presenting an image as usable:

- Confirm the exact pixel dimensions match the requested canvas.
- Confirm the product's shape, color, proportions, labels, and functional details match the source.
- Confirm all visible text is spelled correctly, readable at mobile thumbnail size, and not crowding the product.
- Confirm the image has one clear primary message and is not a pile of selling points.
- For main images, confirm pure white background, no overlay text/graphics, no non-included props, actual product only, and enough product fill.
- For secondary images, confirm claims are truthful and visually supported.
- If any check cannot be verified from the available material, say so clearly rather than implying upload readiness.

## Amazon-Specific Baseline

- Main image: product-only, pure white background, no overlays, no props unless included, professional lighting, product occupying about 85% or more of the frame.
- Secondary images: allow lifestyle, infographics, callouts, size charts, comparison, and usage steps, but keep the product truthful and the claims supportable.
- Default deliverables in this workspace: `2000x2000` for square and `1600x2000` for vertical unless the user requests otherwise.
- Never output below 2K quality for this user's Amazon image work.
- Upload-oriented technical baseline: JPEG/JPG, PNG, or TIFF; RGB or CMYK; at least 1000 px on the longest side for zoom eligibility; include the product identifier in final upload filenames when the user provides it.

## Final Response

Keep responses practical and design-led:

- For plans, list each image with size, purpose, visual direction, and copy.
- For generated files, include the image/file path and a brief quality note.
- Mention any uncertainty about Amazon category-specific rules or claim substantiation.
