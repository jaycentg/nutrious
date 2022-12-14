function getPercentage(needed, collected){
    if(needed <= collected){
        return '100'
    } else{
        let percent = Math.ceil((collected/needed)*100)
        return percent.toString()
    };
};

function loadData(){
    $('#card').empty();
    let data_card ="";
    $.ajax({
        url: "json/",
        type: "GET",
        dataType: "json",
        success: function(resp){
            if (resp.length == 0){
                data_card += `
                        <div class="text-center fw-bold">No Donation</div>
                        <div class="text-center">Verified donations will appear here</div>
                    `
            } else{
                for (let i of resp){
                    let is_Collected = i.fields.amountNeeded <= i.fields.collectedFunds ? "Collected, but you can still donate if your want" : "Still need more donation"
                    let needed_left = i.fields.amountNeeded - i.fields.collectedFunds
                    needed_left = needed_left < 0 ? 0 : needed_left
                    let amountNeeded = parseInt(i.fields.amountNeeded)
                    let collectedFunds = parseInt(i.fields.collectedFunds)
                    let percent = getPercentage(amountNeeded, collectedFunds)
                    data_card +=`
                            <div class="card card-donatee p-2 m-2" id="donatee-${i.pk}">
                                <div class="card-body m-2">
                                    <div class="card-title fw-bold h2">${i.fields.name}</div>
                                    <div class="card-text m-1">Amount Needed: <span class="fw-bold">${rupiah(amountNeeded)}</span></div>
                                    <div class="card-text m-1">Collected Funds: <span class="fw-bold">${rupiah(collectedFunds)}</span></div>
                                    <div class="card-text m-1">Amount left: <span class="fw-bold">${rupiah(parseInt(needed_left))}</span></div>
                                    <div class="card-text m-1">Donation Status: <span class="fw-bold">${is_Collected}</span></div>
                                    <div class="progress mt-3 mx-1">
                                        <div class="progress-bar bg-success" role="progressbar" style="width: ${percent}%" aria-valuenow="${percent}" aria-valuemin="0" aria-valuemax="100"></div>
                                    </div>
                                    <a href="details/${i.pk}" class="stretched-link"></a>
                                </div>
                            </div>
                        `;
                }
            }
            $('#card').append(data_card);
        },
        error: function(resp){
            console.log('Error?');
        }
    })
}

$(document).ready(function(){
    loadData();
});

const rupiah = (number)=>{
    return new Intl.NumberFormat("id-ID", {
        style: "currency",
        currency: "IDR"
    }).format(number);
}