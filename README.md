<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/header-light.svg">
  <img src="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/header-dark.svg" alt="Yuvaraj Vodiboina | Frontend engineer and independent product builder at CodeHorizon. Web interfaces, browser tools, and Android apps." width="100%">
</picture>

<p align="center">
  <a href="https://codehorizon.in/"><img src="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/icon-horizon.svg" width="18" height="18" alt=""> <b>CodeHorizon</b></a> &nbsp; / &nbsp;
  <a href="https://yuvarajvodiboina.in/"><img src="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/icon-web.svg" width="18" height="18" alt=""> <b>Portfolio</b></a> &nbsp; / &nbsp;
  <a href="https://www.linkedin.com/in/yuvarajvodiboina/"><img src="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/icon-network.svg" width="18" height="18" alt=""> <b>LinkedIn</b></a> &nbsp; / &nbsp;
  <a href="mailto:yuvarajvodiboina@gmail.com"><img src="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/icon-mail.svg" width="18" height="18" alt=""> <b>Email</b></a>
</p>

I’m Yuvaraj, a frontend engineer and the developer behind **[CodeHorizon](https://codehorizon.in/)**. I build browser extensions and Android apps, from the interface and platform APIs to store releases and ongoing updates.

The interesting work is in the details: keeping focus settings intact after navigation, reopening saved tabs, wrapping text selections, and making small tools useful offline.

<a href="https://codehorizon.in/products/">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/proof-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/proof-light.svg">
  <img src="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/proof-dark.svg" alt="CodeHorizon catalogue: six live products, two Android apps in testing. Open the product pages and store listings." width="100%">
</picture>
</a>

## Products and the problems behind them

Each product below is live. The project pages include screenshots and product details; the store links let you try the released apps.

<table>
<tr>
<td width="50%" valign="top">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/shopgrade-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/shopgrade-light.svg">
  <img src="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/shopgrade-dark.svg" alt="ShopGrade | Live | CHROME EXTENSION + WEB" width="100%">
</picture>
<p><b>ShopGrade</b> &nbsp; <sub>LIVE</sub></p>
<p><b>Challenge</b><br>An audit needs a clear next action, even though a public storefront cannot reveal orders, traffic, or actual conversion data.</p>
<p><b>How I handled it</b><br>I combined storefront signals and performance checks into a report with evidence and next actions, without requiring admin access. Added sharing and export for client handoffs.</p>
<p><sub>JavaScript / Manifest V3 / Chrome APIs</sub></p>
<p><a href="https://codehorizon.in/products/shopgrade/"><b>Project details</b></a> &nbsp; / &nbsp; <a href="https://chromewebstore.google.com/detail/shopgrade/aenccbnkkimncdjikjgapconaegnmbeo">Chrome Web Store</a></p>
</td>
<td width="50%" valign="top">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/securevault-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/securevault-light.svg">
  <img src="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/securevault-dark.svg" alt="SecureVault | Live | ANDROID / LOCAL FILE VAULT" width="100%">
</picture>
<p><b>SecureVault</b> &nbsp; <sub>LIVE</sub></p>
<p><b>Challenge</b><br>File privacy needs encryption, protected keys, and predictable unlock and lock behavior.</p>
<p><b>How I handled it</b><br>I used AES-256-GCM and Android Keystore, with biometric unlock, passcode fallback, and inactivity locking behind a working calculator.</p>
<p><sub>Kotlin / Jetpack Compose / Android Keystore</sub></p>
<p><a href="https://codehorizon.in/products/securevault/"><b>Project details</b></a> &nbsp; / &nbsp; <a href="https://play.google.com/store/apps/details?id=com.codehorizon.calculator">Google Play</a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/tubefocus-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/tubefocus-light.svg">
  <img src="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/tubefocus-dark.svg" alt="TubeFocus | Live | CHROME / FOCUS + NAVIGATION" width="100%">
</picture>
<p><b>TubeFocus</b> &nbsp; <sub>LIVE</sub></p>
<p><b>Challenge</b><br>YouTube changes pages without a reload. Closing the extension popup should not reset a focus session.</p>
<p><b>How I handled it</b><br>I stored the session end timestamp in Chrome storage, checked expiry in the content script, and reapplied hiding rules after YouTube navigation.</p>
<p><sub>JavaScript / Chrome Storage / MutationObserver</sub></p>
<p><a href="https://codehorizon.in/products/tubefocus/"><b>Project details</b></a> &nbsp; / &nbsp; <a href="https://chromewebstore.google.com/detail/ghmoajebamiileeffdiplohlbgnhnadl">Chrome Web Store</a></p>
</td>
<td width="50%" valign="top">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/tabcluster-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/tabcluster-light.svg">
  <img src="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/tabcluster-dark.svg" alt="TabCluster | Live | CHROME / TABS + WORKSPACES" width="100%">
</picture>
<p><b>TabCluster</b> &nbsp; <sub>LIVE</sub></p>
<p><b>Challenge</b><br>A useful saved workspace needs data that survives the current set of browser tab IDs.</p>
<p><b>How I handled it</b><br>I grouped tabs by domain, added a preview, and stored URLs and titles locally so saved workspaces could be reopened later.</p>
<p><sub>JavaScript / Tabs API / Tab Groups API</sub></p>
<p><a href="https://codehorizon.in/products/tabcluster/"><b>Project details</b></a> &nbsp; / &nbsp; <a href="https://chromewebstore.google.com/detail/faligjbhpbmnajkdpcefhebinddmbmbo">Chrome Web Store</a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/notilo-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/notilo-light.svg">
  <img src="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/notilo-dark.svg" alt="Notilo | Live | CHROME / SELECTION + NOTES" width="100%">
</picture>
<p><b>Notilo</b> &nbsp; <sub>LIVE</sub></p>
<p><b>Challenge</b><br>A text selection can cross several DOM nodes, making a simple highlight wrapper fail.</p>
<p><b>How I handled it</b><br>I used Selection and Range APIs with an extract-and-wrap fallback. Saved notes per page and matched stored text to restore highlights on revisit.</p>
<p><sub>JavaScript / Selection API / Range API</sub></p>
<p><a href="https://codehorizon.in/products/notilo/"><b>Project details</b></a> &nbsp; / &nbsp; <a href="https://chromewebstore.google.com/detail/ocgkllkcodafimnkheijpachancljmdk">Chrome Web Store</a></p>
</td>
<td width="50%" valign="top">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/companion-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/companion-light.svg">
  <img src="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/companion-dark.svg" alt="Companion AI | Live | ANDROID / OFFLINE QUOTES" width="100%">
</picture>
<p><b>Companion AI</b> &nbsp; <sub>LIVE</sub></p>
<p><b>Challenge</b><br>Saved quotes and daily reminders need to remain useful when a network request is unavailable.</p>
<p><b>How I handled it</b><br>I kept quotes and favourites locally, drew reminder content from a cache, and scheduled background work with WorkManager.</p>
<p><sub>Kotlin / Room / WorkManager</sub></p>
<p><a href="https://codehorizon.in/products/companion-ai/"><b>Project details</b></a> &nbsp; / &nbsp; <a href="https://play.google.com/store/apps/details?id=com.codehorizon.companion">Google Play</a></p>
</td>
</tr>
</table>

## Currently in testing

| Product | What it does | Status |
| :--- | :--- | :--- |
| [Speaker Cleaner](https://codehorizon.in/products/speaker-cleaner/) | An Android utility for playing speaker-cleaning tones. | In testing |
| [Nicked](https://codehorizon.in/products/nicked/) | A daily cricket guessing game with six attempts. | In testing |

Release notes and product updates live in the [CodeHorizon changelog](https://codehorizon.in/changelog/).

## Where I spend my time

| Interfaces | Browser platform | Android |
| :--- | :--- | :--- |
| React / Next.js / TypeScript | Manifest V3 / Chrome APIs | Kotlin / Jetpack Compose |
| Tailwind CSS / REST APIs | DOM / Selection / Range | Coroutines / StateFlow |
| Node.js / Firebase | Tabs / Tab Groups / Storage | Room / WorkManager / Keystore |

<details>
<summary><b>More background</b></summary>

Previously a frontend engineer at Truedune Beauty, working on e-commerce interfaces and integrations. I also built [Kalpa Corporate Artz](https://kalpacorporateartz.com/) from Figma to production in React, with GitHub Actions and Cloudflare Pages.

Outside code: Gran Turismo 7 and Valorant.

</details>

<p align="center"><sub>Product work at <a href="https://codehorizon.in/">codehorizon.in</a> / More background at <a href="https://yuvarajvodiboina.in/">yuvarajvodiboina.in</a></sub></p>
