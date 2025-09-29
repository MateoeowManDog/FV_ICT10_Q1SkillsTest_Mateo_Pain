from pyscript import document

menuItems = {
    "Espresso": 50,
    "Latte": 80,
    "Cappuccino": 70,
    "Mocha": 90,
    "Americano": 60
}

def create_order(event=None):

    name = document.getElementById("name").value
    address = document.getElementById("address").value
    contact = document.getElementById("contact").value

    checked = document.querySelectorAll("input[name=items]:checked")
    if not checked:
        document.getElementById("orderSummary").innerText = "⚠️ Please select at least one item."
        return

    items = [f"- {c.value} (₱{menuItems[c.value]})" for c in checked]
    total = sum(menuItems[c.value] for c in checked)

    summary = f"""
Order for: {name}
Address: {address}
Contact: {contact}

Items:
{chr(10).join(items)}

Total: ₱{total}
    """.strip()

    document.getElementById("orderSummary").innerText = summary
