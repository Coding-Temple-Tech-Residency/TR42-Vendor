import React from "react";

function RegisterForm() {
    function handleSubmit(e: React.FormEvent) {
        e.preventDefault();
        console.log("Register form submitted");
    }

    return (
        <form onSubmit={handleSubmit} className="space-y-5">

            <div className="grid grid-cols-2 gap-5">
                <input className="input" placeholder="First Name" />
                <input className="input" placeholder="Last Name" />
            </div>

            <input className="input" placeholder="Email" />
            <input className="input" placeholder="Username" />
            <input className="input" placeholder="Password" />
            <input className="input" placeholder="Confirm Password" />

            <button className="btn-primary mt-4">Next</button>

        </form>
    );
}

export default RegisterForm;