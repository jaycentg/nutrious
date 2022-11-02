function deleteCard(){
    $.get("json/", function(resp) {
      

        for (let i of resp){
            var date = new Date();
            x=i.fields.date
            tanggal = x.slice(8,10)
            if(tanggal<date.getDate()||(date.getDate()==1 && tanggal !=1)){
                $.ajax({
                url: "delete/" + i.pk,
            error: function (data) {
                alert("it didnt work");
        }
    });
            }
        }
    })
}     

function createCard(){
    $('#card').empty();
    let data_card ="";
    $.get("json/", function(resp) {
        var counter_add = 0
        var counter_decrease = 0
        var total = 0
        for (let i of resp){
            if ( i.fields.category == 'Burn Calorie'){
                data_card +=
                `
                <div class="card mb-4 card-calorie">
                    <div class="card-body">
                        <div class="card-title fw-bold h2">${i.fields.category}</div>
                        <div class="card-text m-1">Calorie: ${i.fields.calorie} kkal</div>
                        <div class="card-text m-1">Description: ${i.fields.description}</div>
                        <div class="card-text m-1">Time added: ${i.fields.time}</div>
                        <a href="edit_reduce/${i.pk}" class="btn btn-primary link">Edit</a>
                        <a href="delete/${i.pk}"  class="btn btn-primary link">Delete</a>
                    </div>
                </div>
                `
            }else{
            data_card +=
            `
                <div class="card mb-4 card-calorie">
                    <div class="card-body">
                        <div class="card-title fw-bold h2">${i.fields.category}</div>
                        <div class="card-text m-1">Calorie: ${i.fields.calorie} kkal</div>
                        <div class="card-text m-1">Description: ${i.fields.description}</div>
                        <div class="card-text m-1">Time added: ${i.fields.time}</div>
                        <a href="edit_add/${i.pk}" class="btn btn-primary link">Edit</a>
                        <a href="delete/${i.pk}"  class="btn btn-primary link">Delete</a>
                    </div>
                </div>
                `
            }
            ;
            if(i.fields.is_increasing){
                counter_add += i.fields.calorie
            }else{
                counter_decrease += i.fields.calorie
            }
            total = counter_add - counter_decrease

            document.getElementById('counter_add').innerText = counter_add +' kkal'
            document.getElementById('counter_decrease').innerText = counter_decrease +' kkal'
            document.getElementById('total').innerText = total +' kkal'

        }
        $('#card').append(data_card);
        

    })
}          
$(document).ready(function(){
    var date = new Date();
    document.getElementById('date-info').innerText = date.toDateString();
    document.getElementById('counter_add').innerText = 0
    document.getElementById('counter_decrease').innerText = 0
    document.getElementById('total').innerText = 0
    createCard();
    deleteCard();
    $("#decrease").click(function(e){
        var calorie = $("#input_calorie1").val();
        var description = $("#input_deskripsi1").val();
        var category = 'Burn Calorie'
        var date = new Date();
        var hours = date.getHours();  
        var minutes = "0" + date.getMinutes();
        var seconds = "0" + date.getSeconds(); 
        time =  hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);
        if(calorie=="" || description==""){
            alert("Please fill in the calorie and description!");
            return
        }
        $.post("reduce_calorie/",
        {
            calorie,
            description,
            category,
            time,
            date,
        },
        function(data, status){
            createCard();
            $("#input_deskripsi").val("");
            $("#input_calorie").val("");
            document.getElementById("category1").value;

        });
    });
    $("#add").click(function(e){
        var calorie = $("#input_calorie").val();
        var description = $("#input_deskripsi").val();
        var category = document.getElementById("category").value;
        var date = new Date();
        var hours = date.getHours();  
        var minutes = "0" + date.getMinutes();
        var seconds = "0" + date.getSeconds(); 
        time =  hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);
        if(calorie=="" || description==""){
            alert("Please fill in the calorie and description!");
            return
        }
        $.post("add_calorie/",
        {
            calorie,
            description,
            category,
            time,
            date,
        },
        function(data, status){
            console.log("test6")
            createCard();
            $("#input_deskripsi").val("");
            $("#input_calorie").val("");
            document.getElementById("category").value;
        });
    });
    

});
$('#Test').click(function(e){
    e.preventDefault();
    $('#Modal').modal();
});
$('#Test1').click(function(e){
    e.preventDefault();
    $('#Modal1').modal();
});
$('#closeBtn').click(function(e){
    e.preventDefault();
    $('#Modal').modal('hide');
})
$('#closeBtn').click(function(e){
    e.preventDefault();
    $('#Modal1').modal('hide');
})