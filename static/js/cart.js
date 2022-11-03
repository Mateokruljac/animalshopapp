console.log("Js file working")

var updateButtons = document.getElementsByClassName("update-cart")

for (var i = 0; i < updateButtons.length; i++) {
    updateButtons[i].addEventListener("click",function(){
        var productID = this.dataset.product
        var action = this.dataset.action
        console.log("Product:",productID,"Action:",action)
        if(user == "AnonymousUser"){
            errorAddToCart()
        }else{
            console.log("User",user)
            updateCustomerOrder(productID,action)
        }  
    })
    
}

function updateCustomerOrder(productID,action){
    var url = "members/update-item"
    console.log("User is authenticated! God job!")
    console.log("URL",url)

    fetch(url,{
        method: "POST",
        headers :{
            "Content-Type":"application/json",
            "X-CSRFToken" : csrftoken
        },
        body : JSON.stringify({"productID":productID,"action":action})
    })
    .then((response)  => {
        return response.json()
    })
    .then((data) =>{
        console.log("data:",data)
        location.reload()
    })
}

function errorAddToCart(){
    console.log("Anonymous user.")
    alert("You must be logged in to add an item to the cart.")
}