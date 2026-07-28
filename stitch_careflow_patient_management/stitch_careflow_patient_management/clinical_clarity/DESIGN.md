---
name: Clinical Clarity
colors:
  surface: '#f9f9ff'
  surface-dim: '#cfdaf1'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f3ff'
  surface-container: '#e7eeff'
  surface-container-high: '#dee8ff'
  surface-container-highest: '#d8e3fa'
  on-surface: '#111c2c'
  on-surface-variant: '#424751'
  inverse-surface: '#263142'
  inverse-on-surface: '#ebf1ff'
  outline: '#727783'
  outline-variant: '#c2c6d3'
  surface-tint: '#0e5eaf'
  primary: '#004688'
  on-primary: '#ffffff'
  primary-container: '#0d5eaf'
  on-primary-container: '#c4d9ff'
  inverse-primary: '#a7c8ff'
  secondary: '#006a6a'
  on-secondary: '#ffffff'
  secondary-container: '#8cf3f3'
  on-secondary-container: '#007070'
  tertiary: '#42474b'
  on-tertiary: '#ffffff'
  tertiary-container: '#5a5f62'
  on-tertiary-container: '#d5d9dd'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d5e3ff'
  primary-fixed-dim: '#a7c8ff'
  on-primary-fixed: '#001b3c'
  on-primary-fixed-variant: '#004788'
  secondary-fixed: '#8cf3f3'
  secondary-fixed-dim: '#6fd7d6'
  on-secondary-fixed: '#002020'
  on-secondary-fixed-variant: '#004f4f'
  tertiary-fixed: '#dfe3e7'
  tertiary-fixed-dim: '#c3c7cb'
  on-tertiary-fixed: '#171c1f'
  on-tertiary-fixed-variant: '#43474b'
  background: '#f9f9ff'
  on-background: '#111c2c'
  surface-variant: '#d8e3fa'
typography:
  display-lg:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
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
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 24px
  margin: 32px
---

## Brand & Style
The design system is engineered for professional healthcare environments, prioritizing cognitive ease and emotional stability. The brand personality is **composed, reliable, and precise**. It avoids the sterility of traditional medical software by utilizing soft color transitions and human-centric layouts, ensuring that practitioners feel supported rather than overwhelmed.

The design style is **Corporate Modern with a Soft Edge**. It leverages high-quality whitespace and clear information hierarchy to reduce decision fatigue. By combining structural rigor with subtle roundedness and light-filled surfaces, the system balances the seriousness of clinical data with a modern, approachable SaaS aesthetic.

## Colors
The palette is rooted in **Deep Clinical Blue** and **Teal**, colors that evoke trust and hygiene.
- **Primary Blue:** Used for core navigation, primary actions, and brand presence.
- **Secondary Teal:** Used for secondary interactive elements and data visualization categories.
- **Surface Neutrals:** Backgrounds utilize a very light cool-gray (`#F7FAFC`) to reduce eye strain during long shifts. 
- **Functional Accents:** A balanced **Forest Green** signifies healthy states or successful completions, while a **Soft Coral** provides high-visibility alerts without inducing panic. 

All color combinations for text-on-background must maintain a minimum contrast ratio of 4.5:1 to ensure accessibility in varied lighting conditions found in medical facilities.

## Typography
This design system utilizes a dual-font strategy to maximize readability and hierarchy:
- **Manrope** is used for headlines and display text. Its modern, geometric construction provides a clean, professional look that feels contemporary and high-tech.
- **Inter** is used for all UI elements, labels, and body text. It is a systematic, highly legible font specifically designed for computer screens, ensuring patient records and data tables are easy to scan.

Weight is used sparingly to denote hierarchy. Avoid light weights (under 400) to ensure legibility on lower-resolution medical monitors.

## Layout & Spacing
The layout follows a **Fixed-Fluid Hybrid Grid**. For desktop, content is centered within a 1440px max-width container. 
- **Grid:** A 12-column grid system with 24px gutters.
- **Rhythm:** An 8px linear scale governs all padding and margins. 
- **Density:** The system defaults to "Generous" spacing to prevent data-heavy screens from feeling cluttered. However, a "Compact" mode is supported for data tables, reducing vertical padding by 50%.

Sidebars are fixed at 280px to ensure persistent access to primary navigation, while main content areas reflow to accommodate tablet-landscape orientations.

## Elevation & Depth
The design system uses **Tonal Layers** and **Ambient Shadows** to define hierarchy. 
- **Base Layer:** The application background is the lowest level (`#F7FAFC`).
- **Surface Layer:** White cards (`#FFFFFF`) sit on the base layer, using a subtle 1px border (`#E2E8F0`) rather than heavy shadows to define their boundaries.
- **Elevated Layer:** Active overlays, such as modals or dropdowns, use an ambient, multi-layered shadow (0px 4px 20px rgba(0,0,0,0.08)) to create a sense of floating over the interface.

Avoid high-contrast shadows; the goal is to create a soft, natural depth that mimics paper on a desk.

## Shapes
The shape language is defined by **Medium Roundedness**. 
- Core UI components like buttons and input fields use a **0.5rem (8px)** corner radius.
- Larger containers and cards use a **1rem (16px)** radius to soften the overall appearance of the dashboard.
- Selection indicators (like active states in a sidebar) use a "partial pill" shape where only the inner corners are rounded.

This specific level of rounding is chosen to feel approachable and modern without appearing "childish" or overly casual.

## Components
- **Buttons:** Primary buttons use a solid Primary Blue fill. Secondary buttons use an outline style with a 1.5px border. State changes (hover/active) should be indicated by subtle shifts in tonal value rather than color hue.
- **Input Fields:** Use a white background with a light gray border. On focus, the border transitions to Primary Blue with a 2px soft outer glow (halo).
- **Cards:** The primary container for information. Cards must have a 16px border-radius and use `spacing.md` for internal padding.
- **Chips/Status Tags:** Used for patient status (e.g., "Stable," "Critical"). These use a low-saturation background of the status color (e.g., light green) with a high-saturation text of the same hue to ensure readability.
- **Data Tables:** High-density with subtle row striping. Headers are pinned and use the `label-md` typography style for maximum scannability.
- **Progress Steps:** Used for patient intake forms, utilizing a linear connector and circular indicators to show clear progression.