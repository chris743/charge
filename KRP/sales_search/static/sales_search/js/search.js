window.onload = function() {
    
    let commodities = document.querySelectorAll(".commodity");
    let commodities_child = commodities[0];
    let bagType = document.querySelectorAll(".bagType");
    let type_child = bagType[0];
    let selected_commodity = document.getElementById("commodity-selector");
    let selected_bag = document.getElementById("bagType-selector");
    let search_button = document.getElementById("search");
    let selected_count_size = document.getElementById("countSize-selector");
    let FOB = document.getElementById("fob-input"); 

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
              fob: FOB.value,
              type: selected_bag.value,
              commodity: selected_commodity.value,
              count_size: selected_count_size.value,
            }
        }).done(function(o) {
            console.log("gere")
            
            
            for(const [key, value] of Object.entries(o)){
                console.log(value)
                var commodity_paragraph = document.createElement("p");
                var commodity = document.createTextNode(selected_commodity.value);
                commodity_paragraph.appendChild(commodity);

                var bagType_paragraph = document.createElement("p");
                var bagType = document.createTextNode(selected_bag.value);
                bagType_paragraph.appendChild(bagType);

                var countSize_paragraph = document.createElement("p");
                var countSize = document.createTextNode(selected_count_size.value);
                countSize_paragraph.appendChild(countSize);

                var fob_paragraph = document.createElement("p");
                var fob = document.createTextNode(FOB.value);
                fob_paragraph.appendChild(fob);

                var div = document.getElementById("result");
                div.appendChild(commodity_paragraph);
                div.appendChild(bagType_paragraph);
                div.appendChild(countSize_paragraph);
                div.appendChild(fob_paragraph);
                
            }
        }).fail(function(){
            console.log("no good")
        })
        
        })
}

