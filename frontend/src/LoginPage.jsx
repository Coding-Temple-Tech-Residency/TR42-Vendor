import React, { useState } from "react";

function LoginPage() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [errorMessage, setErrorMessage] = useState("");

    function handleEmailChange(event) {
        setEmail(event.target.value);
    }

    function handlePasswordChange(event) {
        setPassword(event.target.value);
    }

    function handleSubmit(event) {
        event.preventDefault();

        // For now, just show the values in the console
        console.log("Email entered:", email);
        console.log("Password entered:", password);

        // Later we will call the backend here
    }

    return (
        <div style={{ maxWidth: "400px", margin: "40px auto" }}>
            <h2>Login</h2>

            <form onSubmit={handleSubmit}>
                <div style={{ marginBottom: "12px" }}>
                    <label>Email</label>
                    <br />
                    <input
                        type="email"
                        value={email}
                        onChange={handleEmailChange}
                        style={{ width: "100%", padding: "8px" }}
                    />
                </div>

                <div style={{ marginBottom: "12px" }}>
                    <label>Password</label>
                    <br />
                    <input
                        type="password"
                        value={password}
                        onChange={handlePasswordChange}
                        style={{ width: "100%", padding: "8px" }}
                    />
                </div>

                {errorMessage && <p style={{ color: "red" }}>{errorMessage}</p>}

                <button type="submit">Login</button>
            </form>
        </div>
    );
}

export default LoginPage;
