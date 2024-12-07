let getProductsURL = "http://127.0.0.1:5000/getProducts";
let addProductsURL = "http://127.0.0.1:5000/addProducts";
let deleteProductsURL = "http://127.0.0.1:5000/deleteProduct";
let getUnitsURL = "http://127.0.0.1:5000/getUnit";
let setProductDisplay = document.getElementById("setProductDisplay");
let addButton = document.getElementById("addButton");
let unitDropDownDisplay = document.getElementById("unit");
let addStyleUnit = document.getElementById("addStyleUnit");
let submitButton = document.getElementById("submit");
let productName = document.getElementById("productName");
let priceName = document.getElementById("priceName");

collectProductAPI()

async function sendDeleteContent(data) {
    const response = await fetch(deleteProductsURL, {
        method : 'POST',
        headers : {'Content-Type' : 'application/json'},
        body : JSON.stringify(data),
    });
    collectProductAPI()
}

async function sendAddContent(data){
    const response = await fetch(addProductsURL, {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify(data),
    });
}

async function collectProductAPI(){
    const response = await fetch(getProductsURL);
    const data = await response.json();
    displayProduct(data)
}

async function collectUnitAPI(){
    const response = await fetch(getUnitsURL);
    const data = await response.json();
    console.log(data)
    displayUnit(data)
}

function displayProduct(data){
    let display = ""
    data.forEach(element => {
        display += `
                        <tr>
                            <td>${element["product_name"]}</td>
                            <td>${element["unit_name"]}</td>
                            <td>${element["product_price"]}</td>
                            <td><span><i class="bi bi-archive-fill" id="delete${element["product_id"]}" onClick="deleteProduct(${element["product_id"]})"></i></span></td>
                        </tr>
                    `
    });
    setProductDisplay.innerHTML = display;
}

function displayUnit(data){
    element = `<option value="" disabled selected>Select a Unit</option>`;
    data.forEach(unit => {
        element += `
            <option value="${unit["unit_name"]}">${unit["unit_name"]}</option>
        `
    });
    unitDropDownDisplay.innerHTML = element;
}

addButton.addEventListener("click", collectUnitAPI);
addButton.addEventListener("click", function(){
    addStyleUnit.style.display = "block";
});

submitButton.addEventListener("click", function(){
    data = {
        "product_name" : `${productName.value}`,
        "unit" : `${unit.value}`,
        "price" : `${priceName.value}`,
    }
    console.log(data)
    sendAddContent(data);
});

function deleteProduct(id){
    data = {
        "product_id" : id,
    }
    console.log(data);
    sendDeleteContent(data);
}