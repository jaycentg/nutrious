const rupiah = (number)=>{
    return new Intl.NumberFormat("id-ID", {
        style: "currency",
        currency: "IDR"
    }).format(number);
};

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
        url: "json-user/",
        type: "GET",
        dataType: "json",
        success: function(resp){
            if (resp.length == 0){
                data_card += `
                        <div class="text-center fw-bold">No Donation</div>
                        <div class="text-center"> Donations that you create will appear here</div>
                    `
            } else{
                for (let i of resp){
                    //let is_verified= i.fields.is_verified ? `<h5 class="card-text" style="color:#25f314;">Verified</h5>` : `<h5 class="card-text" style="color:red;">Not Verified</h5>`
                    let needed_left = i.fields.amountNeeded - i.fields.collectedFunds
                    needed_left = needed_left < 0 ? 0 : needed_left
                    let amountNeeded = parseInt(i.fields.amountNeeded)
                    let collectedFunds = parseInt(i.fields.collectedFunds)
                    let percent = getPercentage(amountNeeded, collectedFunds)
                    let is_Collected = i.fields.amountNeeded <= i.fields.collectedFunds ? "Collected" : "Not yet collected"
                    let isVerified= i.fields.is_verified ? "Verified" : "Not Verified"
                    data_card +=`
                            <div class="card card-donatee p-2 m-2" id="donatee-${i.pk}">
                                <div class="card-body m-2">
                                    <div class="card-header">
                                        <div class="card-title fw-bold h2">${i.fields.name}</div>
                                        <div class="card-text m-1">Verification status: ${isVerified}</div>
                                    </div>
                                    <div class="card-text m-1">Description: ${i.fields.description}</div>
                                    <div class="card-text m-1">Amount Needed: <span class="fw-bold">${rupiah(amountNeeded)}</span></div>
                                    <div class="card-text m-1">Collected Funds: <span class="fw-bold">${rupiah(collectedFunds)}</span></div>
                                    <div class="card-text m-1">Amount left: <span class="fw-bold">${rupiah(parseInt(needed_left))}</span></div>
                                    <div class="card-text m-1">Donation Status: <span class="fw-bold">${is_Collected}</span></div>
                                    <div class="progress mt-3 mx-1">
                                        <div class="progress-bar bg-success" role="progressbar" style="width: ${percent}%" aria-valuenow="${percent}" aria-valuemin="0" aria-valuemax="100"></div>
                                    </div>
                                    <br>
                                    <button class="btn btn-danger" onclick="closeDonations(${i.pk})">Close Donations</button>
                                </div>
                            </div>
                        `
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

$(document).on('submit', '#form_modal',function(e){
    e.preventDefault();
    $.ajax({
        type:'POST',
        url:"/donation/opened-donatee",
        data:{
            name:$('#id_name').val(),
            description:$('#id_description').val(),
            amountNeeded:$('#id_amountNeeded').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success:function(){
            document.getElementById("form_modal").reset();
            loadData();
        },
    });
});

function closeDonations(val){
    console.log(123);
    $.ajax({
        type :"DELETE",
        csrfmiddlewaretoken: "{{ csrf_token }}",
        url :`/donation/delete/${val}`,
        success: function () {
            console.log(12333);
            loadData();
        },
    })
}