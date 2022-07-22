window.onload = function() {
    let commodities = document.querySelectorAll(".commodity")
    console.log(commodities)

    let child = commodities[0]
    console.log(child)

    child.addEventListener("change", function(e){
        $.ajax({
            type: "POST",
            url: "/search/getBags/",
            data: {
                id: e.target.value,
            }
        }).done((o) => {
            var typeArr = []
            var selector = document.getElementById("bagType-selector");
            if(selector.hasChildNodes){
                while(selector.firstChild){selector.firstChild.remove()}
            }
            for(const [key, type] of Object.entries(o)){
                var el = document.createElement("option");
                el.textContent = type;
                el.value = type;
                selector.appendChild(el)
            }
        })
    }) 

    let bagType = document.querySelectorAll(".bagType")

    let type_child = bagType[0]

    let selected_commodity = document.getElementById("commodity-selector")

    type_child.addEventListener("change", function(e){
        $.ajax({
            type: "POST",
            url: "/search/getCountSize/",
            data: {
                type: e.target.value,
                commodity: selected_commodity.value,
            }
        }).done((o) => {
            var CSArr = []
            var selector = document.getElementById("countSize-selector");
            if(selector.hasChildNodes){
                while(selector.firstChild){selector.firstChild.remove()}
            }
            for(const [key, value] of Object.entries(o)){
                var el = document.createElement("option");
                el.textContent = value;
                el.value = value;
                selector.appendChild(el)
            }
        })
    })
    
    
   }

