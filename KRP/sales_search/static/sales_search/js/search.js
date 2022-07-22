window.onload = function() {
    
    let commodities = document.querySelectorAll(".commodity");
    let commodities_child = commodities[0];
    let bagType = document.querySelectorAll(".bagType");
    let type_child = bagType[0];
    let selected_commodity = document.getElementById("commodity-selector");
    let selected_bag = document.getElementById("bagType-selector");
    let search_button = document.getElementById("search");
    let selected_count_size = document.getElementById("countSize-selector") 

    commodities_child.addEventListener("change", function(e){
        $.ajax({
            type: "POST",
            url: "/search/getBags/",
            data: {
                id: e.target.value,
            }
        }).done((o) => {
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
    type_child.addEventListener("change", function(e){
        $.ajax({
            type: "POST",
            url: "/search/getCountSize/",
            data: {
                type: e.target.value,
                commodity: selected_commodity.value,
            }
        }).done((o) => {
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
    
    search_button.addEventListener("click", function(e){
        $.ajax({
            type: "POST",
            url: "/search/getResults/",
            data: {
              type: selected_bag.value,
              commodity: selected_commodity.value,
              count_size: selected_count_size.value,
            }
        })
        
        })
}

