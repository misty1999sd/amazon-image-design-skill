# Reference-Locked Product Rebuild (Banana)

Use this SOP when a listing image must show the real product with near-photographic fidelity: main images, installed-state shots, angle re-renders of an existing product photo, or any fix where the client says "the product must look exactly like my photo".

This workflow was validated on a real case (Starlink wall-mount bracket main image, 4096x4096, 2026-11-01). The numbers in section 8 are from that case; reuse the method, not the numbers.

## 1. Channel Selection

- Reference fidelity is the goal and the final image carries no text -> use the Banana profile (`nano-banana-pro` first, then `nano-banana-2.1`, then `nano-banana-2`).
- The final image carries any visible text -> use `gpt-image-2`. Text accuracy outranks reference fidelity.
- Never switch providers mid-task without telling the client. Never fall back to the built-in image tool to "rescue" a failed generation.
- When the client says "no local editing", that bans every pixel-level local operation on the deliverable: no resizing, no colour correction, no compositing, no retouching, no re-encode as a design step. Only the model's native full-frame output may be delivered.

## 2. Reference Layering

Lock three kinds of truth, and give the model at most three images:

1. Structure truth: one real photo that shows the whole product at the required angle. This is the only source of geometry, proportions and part layout.
2. Detail truth: one real close-up per contested detail (cable loop, wall-end tail, seam/shading, mount contact). Do not send a close-up for a detail that is not being changed.
3. Optional style anchor: the currently approved render, only when the client accepted it and one isolated attribute must change.

Rules learned the hard way:

- More than three references makes every model drift. Two (structure + one close-up) is the most stable combination.
- Never mix a mirrored or reversed view into the reference set; the model will mirror the whole product.
- Never use a low-detail or highly stylised reference as a composition anchor.

## 3. Base Image Selection Decides The Colour

Every edit re-renders the whole frame, so any defect in the base is inherited and usually amplified.

- Measure the base before using it. A base with a visible cast produces output with a worse cast.
- Chain depth matters: each generation on top of a previous render roughly adds 1.5-2 more levels of tint. Two chained edits is the practical limit.
- If the approved base already carries a cast, do not "edit the cast away". Rebuild from a neutral source instead, or accept the residual and stop.
- A neutral result is far more likely when the first frame is drawn from the real product photo than when it is edited from a previous render.

## 4. One Generation, One Change

- Each generation changes exactly one attribute. Combining two changes (e.g. thinner cable + neutral colour) makes the model re-invent both and fail both.
- State what must not change as a positive preservation list: "preserve the existing sharp near-square corners", not "the corners are not rounded".
- Negative phrasing ("no rounded corners", "no extra cable") is weak compliance. Convert every prohibition into either a preserved named feature or a measurable quantity.
- Quantify in pixels and ratios, not adjectives: "the pole is 204 px wide, the cable must be 20 px wide, about one tenth of the pole", not "make the cable thin".
- Prefer relative instructions when an absolute is unmeasurable: "halve the current thickness" beats "10 px".

## 5. Prompt Skeleton

1. Role declaration: "IMAGE 1 is the approved product photograph. Reproduce it exactly and change ONE thing only."
2. The single change, with quantity and both endpoints ("same start points, same end points, same loop size, only thinner").
3. Preservation list of every visible part by name, plus framing, scale, margins, position, shading and background.
4. Colour guard: "preserve the exact colour of IMAGE 1, identical white balance, exposure and contrast, all greys with equal red, green and blue values, no blue, violet, magenta or warm tint".
5. Background guard: "pure white 255,255,255, no floor shadow, no reflection, no vignette, product fully inside the frame".
6. Invented-content guard: "no label, sticker, text, logo, watermark, screw, connector, extra hole, extra hardware or second cable".

Keep the whole prompt under roughly 2500 characters. Long prompts dilute the single change.

## 6. The Three Failure Modes To Watch

- Component drift: the model "improves" a part you did not ask about (adds a label, changes a bracket, opens a hole). Reject and roll again; do not patch.
- Wash-out: metal parts rendered as mid grey instead of black, so the product looks plastic. Catch it with the true-black ratio metric, not by eye.
- Cast creep: each pass shifts the neutral grey toward violet/blue. Catch it with the green-deficit metric.

## 7. Numeric Acceptance Gate

Run the probe script (`scripts/check_palette.py`) on every candidate. Do not present an image until all of these pass.

| Check | Metric | Pass |
|---|---|---|
| Neutrality | green deficit `G - (R+B)/2` over neutral-grey pixels | within +-2.0 |
| Channel balance | `R - B` over the same pixels | within +-2.5 |
| Background | share of pure white in a 40 px border band | >= 0.99 |
| Nothing clipped | non-white bounding box inside the canvas | margin >= 1.5% per side |
| Real black | share of pixels darker than 30/255 | >= 0.008 (catches wash-out) |
| Canvas | pixel dimensions | exactly the requested size, native |
| Cable gauge (if a cable is modelled) | cable width / pole diameter | 0.10-0.14 |
| Corners (if the product has square corners) | visual check for a tiny chamfer, not a round | pass |

Visual QC for geometry, corners and routing still needs eyes on the file (downscaled vision check is acceptable); the numeric gate only covers tone, framing and scale. When the vision review and the numbers disagree, trust the numbers for tone and framing, and trust the vision review only for part identity.

## 8. Case Record: Starlink Wall-Mount Main Image

- Deliverable: 4096x4096 native JPEG, pure white, product fully inside frame.
- Structure truth: the seller's real listing photo. Detail truth: real close-ups of the pole-bottom loop, wall-end tail, panel seam and mount contact.
- Working base: a clean neutral render accepted by the client for geometry.
- Two client complaints on the rejected version: cable too thick, colour cast.
- Rejected version: green deficit -6.97, cable/pole 0.16.
- Delivered version: green deficit -2.19, cable/pole 0.11, background edge purity 1.00, product bbox 287-3992 within the canvas, true-black ratio 0.013.
- Attempts that failed and why: editing an already-cast base (cast grew to -4.7), fresh text-to-image from the real photo with margins demanded (wash-out: true-black 0.001, metal grey 0.18), close-ups of a detail while also demanding a colour fix (both failed), six generations of "thinner cable" on a wash-out base (cable never thinned).
- Reusable conclusion: fix one attribute per pass, verify with numbers, and stop as soon as both the client's named defects are inside the pass band.

## 9. Delivery

- Write the native file, never resample. Name it with role and size, e.g. `starlink-mount-main-4k.jpg`.
- Report file path, exact pixel size, and the measured values of the checks that mattered.
- State any residual defect and its measured size instead of claiming perfection.
