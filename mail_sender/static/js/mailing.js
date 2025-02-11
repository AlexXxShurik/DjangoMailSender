$(document).ready(function () {
    $("#mailingForm").submit(function (event) {
        event.preventDefault();
        let formData = $(this).serialize();

        $.ajax({
            type: "POST",
            url: "/mailing/create/",
            data: formData,
            success: function (response) {
                if (response.status === "success") {
                    alert("Рассылка отправлена!");
                    $("#mailingModal").modal("hide");
                    $("#mailingForm")[0].reset();
                } else {
                    alert("Ошибка: " + JSON.stringify(response.errors));
                }
            },
            error: function () {
                alert("Ошибка при отправке запроса");
            }
        });
    });
});
