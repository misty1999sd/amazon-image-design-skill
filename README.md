# Amazon Image Design Skill

English | 日本語

## English

Amazon Image Design Skill is a Codex skill for planning, analyzing, generating, revising, and reviewing Amazon listing images and ecommerce product visuals.

It is designed for Amazon operators, designers, and sellers who need marketplace-aware image plans, competitor-informed creative direction, and strict product fidelity when turning product materials into listing images.

### What It Does

- Creates Amazon image design plans for main images, lifestyle images, infographics, comparison images, size charts, package images, A+ visuals, and ecommerce gallery sets.
- Uses market and competitor research when product categories, reference images, Amazon links, reviews, Q&A, or competitor pages are provided.
- Keeps every image focused on one clear visual message instead of piling up selling points.
- Prioritizes scene-based, immersive ecommerce design where appropriate.
- Applies Amazon image compliance baselines for main images and secondary listing images.
- Enforces strict product fidelity: product shape, color, labels, text, proportions, materials, and functional details must match the user's source image.

### Default Output Standards

- Square images: `2000 x 2000 px`
- Vertical 4:5 images: `1600 x 2000 px`
- Other ratios: longest side at least `2000 px`
- Main image: pure white background, product only, no overlays, no props unless included
- Secondary images: lifestyle scenes, concise callouts, size charts, comparison, detail close-ups, and usage steps when truthful and useful

Outputs below 2K quality are treated as unsuitable unless a smaller derivative is explicitly requested.

### Product Fidelity Rules

Product fidelity is the most important rule in this skill.

When a user provides a product image, the product is treated as the locked source of truth:

- Do not deform the product.
- Do not change its color.
- Do not change visible text, labels, logos, ports, seams, stitching, buttons, or functional details.
- Do not invent accessories or included parts.
- Do not change the product function.
- Do not resize the product in a way that makes the scene unrealistic.

If a generated or edited image changes the product's actual appearance, the result is considered unusable and must be revised.

### Repository Structure

```text
amazon-image-design-skill/
|-- SKILL.md
|-- README.md
|-- agents/
|   `-- openai.yaml
`-- references/
    `-- amazon-image-requirements.md
```

### Installation

Copy the `amazon-image-design` skill folder into your Codex skills directory:

```powershell
Copy-Item -Recurse -Force . "$env:USERPROFILE\.codex\skills\amazon-image-design"
```

Then restart Codex so the skill can be discovered.

### Example Prompts

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

### Workflow

1. Confirm the product, marketplace context, image role, ratio, source materials, and any must-use copy.
2. Review Amazon image requirements when upload readiness or main-image compliance matters.
3. Research competitor pages, reference links, reviews, Q&A, and category patterns when available.
4. Propose an original image direction with composition, copy, color, typography, product placement, and compliance notes.
5. Generate or edit the image when requested.
6. Run a quality gate for dimensions, product fidelity, text legibility, visual hierarchy, claim safety, and Amazon compliance.

### Amazon Compliance Reference

The included reference file captures baseline Amazon image requirements and local workspace defaults:

- Pure white main-image background: RGB `255, 255, 255`
- Actual product shown clearly
- Product should fill about 85% or more of the main-image frame
- No badges, borders, watermarks, rating graphics, text overlays, or promotional graphics on main images
- Accepted formats commonly include JPG/JPEG, PNG, and TIFF
- At least 1000 px on the longest side for zoom eligibility
- Category-specific rules may add extra restrictions

For final upload-critical work, verify current Seller Central and category-specific guidance because Amazon requirements and enforcement can change.

---

## 日本語

Amazon Image Design Skill は、Amazon 商品画像とEC向け商品ビジュアルの企画、分析、生成、修正、レビューを支援する Codex スキルです。

商品素材を Amazon のリスティング画像に落とし込む際に、マーケットプレイス要件、競合分析に基づくクリエイティブ設計、そして厳格な商品外観の保持を重視します。

### 主な機能

- メイン画像、ライフスタイル画像、インフォグラフィック、比較画像、サイズ表、パッケージ画像、A+ コンテンツ、ECギャラリー画像の設計案を作成します。
- 商品カテゴリ、参考画像、Amazonリンク、レビュー、Q&A、競合ページが提供された場合、マーケットと競合を分析してデザイン方針に反映します。
- 1枚の画像につき、明確な主メッセージを1つに絞り、売り文句の詰め込みを避けます。
- 必要に応じて、シーン性と没入感のあるECデザインを優先します。
- Amazon のメイン画像およびサブ画像に関する基本的なコンプライアンス要件を考慮します。
- 商品の形状、色、ラベル、文字、比率、素材感、機能的ディテールが、ユーザー提供の元画像と一致するよう厳格に扱います。

### デフォルト出力基準

- 正方形画像: `2000 x 2000 px`
- 縦長 4:5 画像: `1600 x 2000 px`
- その他の比率: 長辺を最低 `2000 px`
- メイン画像: 純白背景、商品単体、オーバーレイなし、同梱されない小物なし
- サブ画像: ライフスタイルシーン、簡潔な訴求、サイズ表、比較、ディテール拡大、使用手順などを、事実に基づいて必要な場合に使用

明示的に小さい派生画像を求められた場合を除き、2K未満の品質は Amazon 用画像として不適切とみなします。

### 商品外観保持ルール

商品外観の保持は、このスキルで最も重要なルールです。

ユーザーが商品画像を提供した場合、その画像を唯一の正しい基準として扱います。

- 商品を変形しない。
- 色を変更しない。
- 表示されている文字、ラベル、ロゴ、ポート、縫い目、ステッチ、ボタン、機能的ディテールを変更しない。
- 付属していないアクセサリーや内容物を追加しない。
- 商品の機能を変更しない。
- シーン内で不自然に見えるほど商品サイズを変えない。

生成または編集された画像で商品の実際の外観が変わった場合、その出力は使用不可とみなし、修正が必要です。

### リポジトリ構成

```text
amazon-image-design-skill/
|-- SKILL.md
|-- README.md
|-- agents/
|   `-- openai.yaml
`-- references/
    `-- amazon-image-requirements.md
```

### インストール

`amazon-image-design` スキルフォルダを Codex のスキルディレクトリにコピーします。

```powershell
Copy-Item -Recurse -Force . "$env:USERPROFILE\.codex\skills\amazon-image-design"
```

その後、Codex を再起動するとスキルが認識されます。

### 使用例

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

### ワークフロー

1. 商品、販売マーケット、画像の役割、比率、元素材、必須コピーを確認します。
2. アップロード可否やメイン画像の適合性が重要な場合、Amazon 画像要件を確認します。
3. 競合ページ、参考リンク、レビュー、Q&A、カテゴリ内の表現傾向を必要に応じて調査します。
4. 構図、コピー、配色、タイポグラフィ、商品配置、コンプライアンス上の注意点を含む独自の画像方針を提案します。
5. ユーザーが求めた場合、画像を生成または編集します。
6. サイズ、商品外観の一致、文字の可読性、視覚階層、訴求の安全性、Amazon 画像要件を品質チェックします。

### Amazon 画像要件の参考

同梱の参考ファイルには、Amazon 画像要件の基本基準と、このワークスペースでのローカル基準をまとめています。

- メイン画像の背景は純白: RGB `255, 255, 255`
- 実際に販売される商品を明確に表示
- メイン画像では商品がフレームの約85%以上を占めること
- メイン画像ではバッジ、枠線、透かし、評価グラフィック、テキストオーバーレイ、販促グラフィックを使用しない
- 一般的に JPG/JPEG、PNG、TIFF 形式が使用可能
- ズーム対象にするには、長辺が最低1000px必要
- カテゴリごとに追加ルールが存在する場合があります

最終アップロードを前提とする作業では、Amazon の要件や運用が変わる可能性があるため、現在の Seller Central とカテゴリ別ガイドラインを確認してください。
