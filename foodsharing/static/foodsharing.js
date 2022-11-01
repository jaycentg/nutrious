function createCard() {
    console.log("masukkkk")
    console.log(`{{user}}`)
    $('#card').empty();
    let data_card = "";

    let button = "";
    $.get("json/", function (resp) {
        if (resp.length == 0) {
            data_card = `<div class="p-4">
                <div class="card mb-1 text-bg-light">
                            <div class="card-body">
                                <div class="col bg-light text-center">
                                <h5 class="card-title">There is no post</h5>
                                </div>
                        </div>
                    </div>
                </div>
            `

        }
        else {
            for (let i of resp) {

                if (`{{user.is_user}}`) {
                    if (($("#current_user").val()) == `${i.fields.author}`) {
                        button = `<a data-id="${i.pk}" class="btn btn-outline-primary p-2 m-1" data-bs-toggle="modal"
                                    data-bs-target="#edit-modal" id="edit-modal-btn">Edit</a>
                        <a href="delete/${i.pk}" class="btn btn-outline-primary p-2 m-1">Delete</a>`

                    }
                }
                data_card += ` 
            <div class="p-3" id="per_satuan">
                <div class="card mb-3 text-bg-light">
                    <div class="row g-0">
                        <div class="col-md-4 bg-light text-center" style="width: md-4;">
                            <img src=${i.fields.img}
                                class="img-fluid rounded-start" style="width: 100%; height: 100%; object-fit: cover;">
                                
                        </div>
                        <div class="col-md-8">
                            <div class="card-body">
                                <h5 class="card-title"><b>Locatian at:</b> ${i.fields.location}</h5>
                                <p class="card-text"><b>Description : </b> ${i.fields.description}</p>
                                <br>
                             
                                <p class="card-text"><small>Post Date: ${i.fields.date}</small></p>
                                <p class="card-text"><small>Last Edit: ${i.fields.update_date}</small></p>
                                
                                ${button}
                            </div>
                    </div>
                    </div>
                </div>
            </div>
            `
                button = "";

            };
        }

        $('#card').append(data_card);



    })
}

$(document).ready(function () {
    var id = $(this).data;
    console.log(id)
    createCard();
    function validate() {
        if ($('#input_location').val().length > 0 &&
            $('#input_description').val().length > 0 &&
            $('#input_image').val().length > 0) {
            $("#Send-footer").prop("disabled", false);
        }
        else {
            $("#Send-footer").prop("disabled", true);
        }
    }

    $("#create_post").click(function (e) {
        console.log("ada masuk");
        var location = $("#input_location").val();
        var description = $("#input_description").val();
        var img = $("#input_image").val();
        validate();
        console.log(location)
        $.post("add_location/",
            {
                location,
                description,
                img,
            },

            function (data, status) {
                createCard();
                console.log("create card success");
                $("#input_location").val("");
                $("#input_description").val("");
                $("#input_image").val("");
                $('#Modal').modal('hide');
            });

    });

    $("#edit_post").click(function (e) {

        console.log("ini kan");

        var pk = $("#input_pk").val();
        console.log(pk)

        var location = $("#input_location_edit").val();
        var description = $("#input_description_edit").val();
        var img = $("#input_image_edit").val();
        validate();
        console.log("ini kan yg edit", location)
        $.ajax({
            url: `edit_add_save/${pk}`,
            headers: { 'X-CSRFToken': '{{ csrf_token }}' },
            data: {
                location,
                description,
                img,
            },
            method: "POST",
            success: function (data, status) {
                console.log("edit card success");
                $("#input_location_edit").val("");
                $("#input_description_edit").val("");
                $("#input_image_edit").val("");
                createCard();
                $('#edit-modal').modal('hide');
            },

        });

    });
});

$(document).on('click', '#edit-modal-btn', function (e) {
    e.preventDefault();
    edit_id = $(this).attr("data-id");
    $.ajax({
        url: `edit_add/${edit_id}`,
        method: "GET",

        success: function (data) {
            data = JSON.parse(data);

            $("#input_location_edit").val(data.location);
            $("#input_description_edit").val(data.description);
            $("#input_image_edit").val(data.img);
            $("#input_pk").val(data.pk);
            $('#edit-modal').modal('show');
        }
    })

})

$('#modal-btn').click(function (e) {
    e.preventDefault();
    console.log("ya masuk la")
    $('#Modal').modal();
});

// $('#edit-modal-btn').click(function (e) {
// // $('[id^="edit-modal-btn"]').click(function (e) {
//     e.preventDefault();
//     $('#edit-modal').modal();
//     console.log("uda panggil ya ges ya");
//     var pk = $(this).data("data-id");
//     console.log(pk);
// });

$('#close-modal').click(function (e) {
    e.preventDefault();
    $('#Modal').modal("hide");
});

$('#close-edit-modal').click(function (e) {
    e.preventDefault();
    $('#edit-modal').modal("hide");
});
