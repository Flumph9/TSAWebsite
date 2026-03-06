let allResources = [];

function showLoading(state) {
  const el = document.getElementById("loading");
  el.style.display = state ? "block" : "none";
}

async function loadResources() {
  showLoading(true);

  const res = await fetch("/all_resources/");
  const data = await res.json();

  const restaurants = data.restaurants || [];
  const groceries = data.grocery_stores || [];
  const gas = data.gas_stations || [];
  const services = data.community_services || [];
  const schools = data.schools || [];

  allResources = [
    ...restaurants,
    ...groceries,
    ...gas,
    ...services,
    ...schools,
  ];

  renderResources(allResources);
  showLoading(false);
}

function renderResources(resources) {
  const container = document.getElementById("results");
  container.innerHTML = "";

  if (resources.length === 0) {
    container.innerHTML = "No results found";
    return;
  }

  resources.forEach((r) => {
    const card = document.createElement("div");
    card.className = "card";

    const title = document.createElement("div");
    title.className = "card-title";
    title.textContent = r.name;

    const btn = document.createElement("button");
    btn.textContent = "Show Details";

    const details = document.createElement("div");
    details.className = "details";

    details.innerHTML = `
      <b>Address:</b> ${r.address || "Unknown"}<br>
      <b>Hours:</b> ${r.hours || "Unknown"}<br>
      ${r.type ? "<b>Type:</b> " + r.type + "<br>" : ""}
      ${r.phone ? "<b>Phone:</b> " + r.phone + "<br>" : ""}
      ${r.reviews ? "<b>Rating:</b> " + r.reviews + "<br>" : ""}
      ${r.price_per_person ? "<b>Price:</b> " + r.price_per_person + "<br>" : ""}
      ${r.website_link ? `<a href="${r.website_link}" target="_blank">Visit Website</a>` : ""}
    `;

    btn.onclick = () => {
      details.style.display = details.style.display === "block" ? "none" : "block";
    };

    card.appendChild(title);
    card.appendChild(btn);
    card.appendChild(details);

    container.appendChild(card);
  });
}

document.getElementById("searchBox").addEventListener("input", function () {
  const term = this.value.toLowerCase();
  const filtered = allResources.filter((r) =>
    (r.name || "").toLowerCase().includes(term)
  );
  renderResources(filtered);
});

/*function createButtons() {
  const container = document.getElementById("buttons");

  const categories = [
    "All Resources",
    "Restaurants",
    "Grocery Stores",
    "Gas Stations",
    "Community Services",
    "Schools",
  ];

  categories.forEach((cat) => {
    const btn = document.createElement("button");
    btn.textContent = cat;
    btn.onclick = () => renderResources(allResources);
    container.appendChild(btn);
  });
}*/

document.getElementById("resourceForm").addEventListener("submit", function (e) {
  e.preventDefault();
  document.getElementById("formStatus").textContent = "Thanks! Your suggestion was recorded.";
  this.reset();
});

loadResources();