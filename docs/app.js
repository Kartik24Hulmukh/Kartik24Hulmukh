const records = [
  {
    n: "01",
    type: ["product"],
    title: "RGIT Rozgar",
    role: "Founder · Product Engineer · Operator",
    claim:
      "A deployed campus resource platform for accommodation, resale, academics, food, and nearby healthcare.",
    evidence: "Live product and public source repository.",
    boundary: "Campus-specific; adoption figures published only when measured.",
    href: "https://rgitrozgar.in",
  },
  {
    n: "02",
    type: ["system", "boundary"],
    title: "Kairo-Phantom",
    role: "Lead Builder · Maintainer · Pre-launch",
    claim:
      "A local-first agent with human confirmation and signed, hash-chained action records.",
    evidence: "Published benchmark, test commands, separately runnable verifier.",
    boundary: "Repository evidence; third-party validation pending.",
    href: "https://github.com/Kartik24Hulmukh/Kairo-Phantom",
  },
  {
    n: "03",
    type: ["system", "boundary"],
    title: "Project X-Ray India",
    role: "Engineering Contributor · Public beta",
    claim:
      "Source-linked public-infrastructure claims organized for human investigation.",
    evidence: "Repository, evidence policy, review gates.",
    boundary: "Supports investigation; does not determine corruption.",
    href: "https://github.com/Kartik24Hulmukh/project-xray-india",
  },
  {
    n: "04",
    type: ["system", "boundary"],
    title: "Proving Grounds",
    role: "Builder · Contributor · Experimental",
    claim:
      "Behavioral claims tested across code revisions with replayable evidence capsules.",
    evidence: "Repository examples and replay paths.",
    boundary: "Bounded executable evidence, not formal proof.",
    href: "https://github.com/KairoPhantom/Proving-Grounds",
  },
];

const root = document.querySelector("#records");
const buttons = Array.from(document.querySelectorAll("nav button"));

function render(filter = "all") {
  const filtered = records.filter(
    (r) => filter === "all" || r.type.includes(filter)
  );
  if (!filtered.length) {
    root.innerHTML = '<p class="empty">No records match this filter.</p>';
    return;
  }
  root.innerHTML = filtered
    .map(
      (r) => `<article class="record">
  <div class="number" aria-hidden="true">${r.n}</div>
  <div>
    <p class="role">${r.role}</p>
    <h2>${r.title}</h2>
    <p>${r.claim}</p>
    <a href="${r.href}">Inspect public record →</a>
  </div>
  <div class="evidence">
    <strong>Evidence</strong>
    <p>${r.evidence}</p>
    <strong>Boundary</strong>
    <p>${r.boundary}</p>
  </div>
</article>`
    )
    .join("");
}

buttons.forEach((button) => {
  button.addEventListener("click", () => {
    buttons.forEach((x) => x.classList.remove("active"));
    button.classList.add("active");
    render(button.dataset.filter);
  });
});

render();
