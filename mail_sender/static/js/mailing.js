$(document).ready(function () {
    function getCSRFToken() {
        return document.cookie.split('; ')
            .find(row => row.startsWith('csrftoken='))
            ?.split('=')[1];
    }

    $("#mailingForm").submit(function (event) {
        event.preventDefault();
        let formData = $(this).serialize();

        $.ajax({
            type: "POST",
            url: "/create/",
            data: formData,
            headers: {
                "X-CSRFToken": getCSRFToken()
            },
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
