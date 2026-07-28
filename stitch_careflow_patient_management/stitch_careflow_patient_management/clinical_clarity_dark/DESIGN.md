---
name: Clinical Clarity Dark
colors:
  surface: '#10131a'
  surface-dim: '#10131a'
  surface-bright: '#363941'
  surface-container-lowest: '#0b0e15'
  surface-container-low: '#181c23'
  surface-container: '#1c2027'
  surface-container-high: '#272a31'
  surface-container-highest: '#31353d'
  on-surface: '#e0e2ec'
  on-surface-variant: '#c1c6d6'
  inverse-surface: '#e0e2ec'
  inverse-on-surface: '#2d3038'
  outline: '#8b919f'
  outline-variant: '#414754'
  surface-tint: '#a9c7ff'
  primary: '#a9c7ff'
  on-primary: '#003063'
  primary-container: '#3d90ff'
  on-primary-container: '#002957'
  inverse-primary: '#005db7'
  secondary: '#a7c8ff'
  on-secondary: '#003061'
  secondary-container: '#0059aa'
  on-secondary-container: '#b9d2ff'
  tertiary: '#ffb68c'
  on-tertiary: '#532200'
  tertiary-container: '#e76e0d'
  on-tertiary-container: '#481d00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#a9c7ff'
  on-primary-fixed: '#001b3d'
  on-primary-fixed-variant: '#00468c'
  secondary-fixed: '#d5e3ff'
  secondary-fixed-dim: '#a7c8ff'
  on-secondary-fixed: '#001b3c'
  on-secondary-fixed-variant: '#004788'
  tertiary-fixed: '#ffdbc9'
  tertiary-fixed-dim: '#ffb68c'
  on-tertiary-fixed: '#321200'
  on-tertiary-fixed-variant: '#753400'
  background: '#10131a'
  on-background: '#e0e2ec'
  surface-variant: '#31353d'
typography:
  headline-lg:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-sm:
    fontFamily: Manrope
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Manrope
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 14px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
---

## Brand & Style
This design system focuses on high-stakes medical and healthcare environments where cognitive load must be minimized. The brand personality is clinical, precise, and authoritative, yet calming. By utilizing a dark aesthetic, the system reduces eye strain for clinicians working in low-light environments or during long shifts.

The design style is **Corporate / Modern** with a lean toward **Minimalism**. It prioritizes information density and legibility through structured layouts and a restrained use of color. Visual interest is generated through subtle tonal shifts rather than decorative elements, ensuring the focus remains entirely on patient data and diagnostic tools.

## Colors
The palette is engineered for clinical precision. The primary background uses a deep navy-charcoal (#0a0c10) to provide a non-distracting canvas. UI containers and cards utilize #161b22 to create a subtle sense of depth.

The primary brand blue has been shifted to a more vibrant #2188ff for interactive elements to ensure AAA accessibility contrast ratios against the dark surfaces, while the deeper #0d5eaf is reserved for secondary states or large-scale brand moments. Status colors (Success/Error) are calibrated for high visibility without being overly neon, maintaining the professional tone of the design system.

## Typography
Manrope is the sole typeface for this design system, chosen for its modern geometric construction and excellent legibility in technical contexts. 

Headlines use tighter letter spacing and bolder weights to establish a clear hierarchy. Body text is optimized with generous line heights to ensure readability of long-form medical reports. Label styles use increased tracking and uppercase transforms to distinguish metadata and tabular headers from primary content.

## Layout & Spacing
The layout follows a **Fluid Grid** model based on a 4px baseline shift. Most components and layouts align to an 8px stepping scale.

- **Desktop:** 12-column grid with 24px gutters and 48px outer margins.
- **Tablet:** 8-column grid with 24px gutters and 32px outer margins.
- **Mobile:** 4-column grid with 16px gutters and 16px outer margins.

Spacing is used to group related clinical data. Use larger gaps (40px+) to separate distinct patient cases or diagnostic categories, while using tighter spacing (8px-16px) for internal form elements and data labels.

## Elevation & Depth
In this dark mode environment, depth is communicated through **Tonal Layers** rather than heavy shadows. 

1. **Floor:** #0a0c10 (The primary background).
2. **Level 1:** #161b22 (Cards, content sections, and navigation sidebars).
3. **Level 2:** #30363d (Hover states, active menu items, and popovers).

Outlines are preferred over shadows for defining component boundaries. Use a 1px "ghost border" with 15% white opacity to define interactive elements like input fields and buttons. This maintains a crisp, "medical-grade" look that remains visible on high-brightness monitors.

## Shapes
The shape language is defined by a consistent **8px (0.5rem) corner radius**, providing a "Rounded" feel that softens the technical nature of the data without appearing informal.

- **Standard Elements:** 8px radius (Buttons, Inputs, Cards).
- **Large Containers:** 16px (1rem) radius (Modals, main content area).
- **Small Elements:** 4px (0.25rem) radius (Tags, tooltips).

## Components
- **Buttons:** Primary buttons use the high-contrast blue (#2188ff) with white text. Secondary buttons use a transparent background with a #30363d border.
- **Input Fields:** Fields are filled with the surface-container color (#161b22) and feature a 1px border. Focus states must trigger a 2px stroke in the primary brand blue.
- **Cards:** Use a flat style with the #161b22 background. Use a subtle top-border color-coding (e.g., Green for "Stable", Red for "Critical") to categorize patient data quickly.
- **Chips/Tags:** Small, low-contrast pills used for medical terminology or status indicators. Use #30363d as the background with the secondary text color.
- **Lists/Tables:** Use alternating row highlights (Zebra striping) with #0d1117 and #161b22 to improve horizontal tracking across dense data sets.
- **Data Visualizations:** Charts should use a specific palette of "Clinical Accents" that are color-blind friendly and stand out clearly against the dark UI surfaces.