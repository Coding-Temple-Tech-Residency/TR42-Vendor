// import RegisterForm from "../forms/RegisterForm";
// import AuthLayout from "../components/AuthLayout";
// import AuthCard from "../components/AuthCard";
// import AuthHeader from "../components/AuthHeader";
// import Logo from "../../../assets/logo.svg";

// function RegisterPage() {
//   return (
//     <AuthLayout>

//       <div className="w-full max-w-2xl">

//         {/* YOUR HEADER (kept from old design) */}
//         <div className="bg-gradient-to-r from-gray-200 to-gray-100 py-6 px-8 rounded-t-xl border-b flex items-center justify-center">
//           <img
//             src={Logo}
//             alt="Field Force Logo"
//             className="h-16 w-auto object-contain"
//           />
//         </div>

//         {/* AUTH CARD */}
//         <AuthCard>
//           <AuthHeader
//             title="Step 1 of 2: Create Your Account"
//             subtitle="Enter your personal details to get started."
//           />

//           <RegisterForm />
//         </AuthCard>

//       </div>

//     </AuthLayout>
//   );
// }

// export default RegisterPage;

import AuthLayout from "../components/AuthLayout";
import AuthCard from "../components/AuthCard";
import AuthHeader from "../components/AuthHeader";
import RegisterForm from "../forms/RegisterForm";
import AuthFooterLink from "../components/AuthFooterLink";

function RegisterPage() {
  return (
    <AuthLayout>
      <AuthCard>
        <AuthHeader
          title="Step 1 of 2: Create Your Account"
          subtitle="Enter your personal details to get started."
        />

        <RegisterForm />

        {/* Footer Link */}
        <AuthFooterLink
          text="Already have an account?"
          linkText="Login"
          to="/login"
        />
        
      </AuthCard>
    </AuthLayout>
  );
}

export default RegisterPage;