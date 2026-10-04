<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v4/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v4/header-light.svg">
  <img src="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v4/header-dark.svg" alt="Yuvaraj Vodiboina. Frontend engineer and independent product developer. Web interfaces, Chrome extensions, and Android apps." width="100%">
</picture>

<p align="center">
  <a href="https://yuvarajvodiboina.in/"><img src="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/icon-web.svg" width="18" height="18" alt=""> <b>Portfolio</b></a> &nbsp; / &nbsp;
  <a href="https://codehorizon.in/"><img src="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/icon-horizon.svg" width="18" height="18" alt=""> <b>CodeHorizon</b></a> &nbsp; / &nbsp;
  <a href="https://www.linkedin.com/in/yuvarajvodiboina/"><img src="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/icon-network.svg" width="18" height="18" alt=""> <b>LinkedIn</b></a> &nbsp; / &nbsp;
  <a href="mailto:yvodiboina@gmail.com"><img src="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v2/icon-mail.svg" width="18" height="18" alt=""> <b>Email</b></a>
</p>

I'm Yuvaraj, a frontend engineer and the developer behind **[CodeHorizon](https://codehorizon.in/)**. I build web interfaces, Chrome extensions, and Android apps, taking the work from design and platform integration through release and subsequent updates.

My projects have taught me to pay attention to the details behind the interface: state after navigation, selections across DOM nodes, encrypted storage, and what happens when the network is unavailable.

<a href="https://codehorizon.in/products/">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v4/proof-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v4/proof-light.svg">
  <img src="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v4/proof-dark.svg" alt="Four live Chrome extensions and two Android apps. Kalpa Corporate Artz client website. Nicked and Speaker Cleaner in testing." width="100%">
</picture>
</a>

## Selected work and engineering decisions

The links below lead to working products, store listings, and project pages with screenshots.

<table>
<tr>
<td width="50%" valign="top">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v4/shopgrade-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v4/shopgrade-light.svg">
  <img src="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v4/shopgrade-dark.svg" alt="ShopGrade / LIVE / CHROME EXTENSION + WEB" width="100%">
</picture>
<p>Shopify storefront audits with reports agencies can share with clients.</p>
<p><b>The challenge</b><br>Useful recommendations have to come from public storefront evidence, without access to orders or traffic data.</p>
<p><b>What I implemented</b><br>I organized observable signals into evidence and prioritized actions. Added report sharing, branded exports, and client presentation decks.</p>
<p><sub>JavaScript / Manifest V3 / Web APIs</sub></p>
<p><a href="https://codehorizon.in/products/shopgrade/"><b>Project details</b></a> &nbsp; / &nbsp; <a href="https://chromewebstore.google.com/detail/shopgrade/aenccbnkkimncdjikjgapconaegnmbeo">Chrome Web Store</a></p>
</td>
<td width="50%" valign="top">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v4/kalpa-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v4/kalpa-light.svg">
  <img src="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v4/kalpa-dark.svg" alt="Kalpa Corporate Artz / LIVE WEBSITE / CLIENT WEBSITE / NEXT.JS" width="100%">
</picture>
<p>An art studio website for exploring artwork and arranging a consultation.</p>
<p><b>The challenge</b><br>The gallery and consultation journey needed clear paths from browsing to making an enquiry.</p>
<p><b>What I implemented</b><br>I took the Figma designs into Next.js and React, organized artwork by style, and built a guided booking flow.</p>
<p><sub>Next.js / React / TypeScript / Figma</sub></p>
<p><a href="https://kalpacorporateartz.com/"><b>Visit the website</b></a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v4/tubefocus-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v4/tubefocus-light.svg">
  <img src="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v4/tubefocus-dark.svg" alt="TubeFocus / LIVE / CHROME / NAVIGATION + STATE" width="100%">
</picture>
<p>A calmer YouTube interface with configurable hiding rules and timed focus sessions.</p>
<p><b>The challenge</b><br>YouTube navigates without a full reload, while an extension popup exists only while it is open.</p>
<p><b>What I implemented</b><br>I stored an absolute session end time in Chrome storage. The content script checks expiry and reapplies the hiding rules after navigation.</p>
<p><sub>JavaScript / Chrome Storage / MutationObserver</sub></p>
<p><a href="https://codehorizon.in/products/tubefocus/"><b>Project details</b></a> &nbsp; / &nbsp; <a href="https://chromewebstore.google.com/detail/ghmoajebamiileeffdiplohlbgnhnadl">Chrome Web Store</a></p>
</td>
<td width="50%" valign="top">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v4/securevault-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v4/securevault-light.svg">
  <img src="https://raw.githubusercontent.com/yuvarajvodiboina/yuvarajvodiboina/main/assets/v4/securevault-dark.svg" alt="SecureVault / LIVE / ANDROID / ENCRYPTION + UX" width="100%">
</picture>
<p>An encrypted Android file vault behind a working calculator.</p>
<p><b>The challenge</b><br>File privacy depends on protected keys, predictable locking, and an unlock flow people can understand.</p>
<p><b>What I implemented</b><br>I used AES-256-GCM and Android Keystore, with biometric unlock, passcode fallback, and inactivity locking. Recent work clarified the passcode setup wording.</p>
<p><sub>Kotlin / Jetpack Compose / Android Keystore</sub></p>
<p><a href="https://codehorizon.in/products/securevault/"><b>Project details</b></a> &nbsp; / &nbsp; <a href="https://play.google.com/store/apps/details?id=com.codehorizon.calculator">Google Play</a></p>
</td>
</tr>
</table>

## More released tools

| Project | The problem and implementation |
| :--- | :--- |
| **[TabCluster](https://codehorizon.in/products/tabcluster/)**<br>[Chrome Web Store](https://chromewebstore.google.com/detail/faligjbhpbmnajkdpcefhebinddmbmbo) | Saved workspaces need to survive the original tabs. I stored URLs and titles locally for reopening, grouped tabs by domain, and added a preview before grouping. |
| **[Notilo](https://codehorizon.in/products/notilo/)**<br>[Chrome Web Store](https://chromewebstore.google.com/detail/ocgkllkcodafimnkheijpachancljmdk) | Text selections can cross DOM nodes. I used Selection and Range APIs with an extract-and-wrap fallback, saved notes per page, and used stored text to restore highlights on revisit. |
| **[Companion AI](https://codehorizon.in/products/companion-ai/)**<br>[Google Play](https://play.google.com/store/apps/details?id=com.codehorizon.companion) | Quotes, favourites, and reminders need to remain useful offline. I used Room for local data and WorkManager to schedule reminders from cached content. |

## What I'm working on

**[Nicked](https://codehorizon.in/products/nicked/)** is a daily cricket guessing game with six attempts and a timed Run Chase mode. **[Speaker Cleaner](https://codehorizon.in/products/speaker-cleaner/)** is a tone-based Android utility. Both are currently in Google Play testing.

Recent release work includes branded client decks and sharing controls in ShopGrade, plus clearer passcode setup in SecureVault. The [CodeHorizon changelog](https://codehorizon.in/changelog/) records the releases and what changed.

## Tools I use

| Web interfaces | Browser platform | Android |
| :--- | :--- | :--- |
| React, Next.js, TypeScript | JavaScript, Manifest V3 | Kotlin, Jetpack Compose |
| Figma, Tailwind CSS, REST APIs | Chrome APIs, DOM, Selection, Range | Room, WorkManager, Android Keystore |

<details>
<summary><b>Earlier experience and public work</b></summary>

Previously a frontend engineer at Truedune Beauty, working on e-commerce interfaces and integrations.

My public Android work includes [AxionAOSP for Xiaomi Pad 6](https://github.com/yuvarajvodiboina/axion-pipa), with the published community build, device integration notes, installation documentation, and upstream credits.

</details>

<p align="center"><sub>Explore the <a href="https://codehorizon.in/products/">product catalogue</a>, read the <a href="https://codehorizon.in/changelog/">release history</a>, or visit my <a href="https://yuvarajvodiboina.in/">portfolio</a>.</sub></p>
