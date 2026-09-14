

from pyscript import document, display


def create_order(e):
    number1 = float(document.getElementById("item1").value) * document.getElementById("item1").checked
    number2 = float(document.getElementById("item2").value) * document.getElementById("item2").checked
    number3 = float(document.getElementById("item3").value) * document.getElementById("item3").checked
    number4 = float(document.getElementById("item4").value) * document.getElementById("item4").checked
    number5 = float(document.getElementById("item5").value) * document.getElementById("item5").checked

    subtotal = number1 + number2 + number3 + number4 + number5
    vat = float(subtotal * 0.12)

    document.getElementById('subtotal').innerHTML = " "
    display(f"subtotal: {subtotal}, tax: {vat}, total: {subtotal + vat}", target="subtotal")