import { RouterProvider } from "react-router-dom";
import { routers } from "./routes";
import { Suspense } from "react";
import { Loader } from "./components";
import { Provider } from "react-redux";
import { store } from "./store";
import { AuthProvider } from "./contexts";
import "./App.scss";
import { listenToAutoSignInEvent } from "./helpers/cognitoServices";
import { Amplify } from "aws-amplify";
import awsConfigs from "./aws-exports";

Amplify.configure(awsConfigs);

listenToAutoSignInEvent();
const App = () => {
  return (
    <Suspense fallback={<Loader />}>
      <Provider store={store}>
        <AuthProvider>
          <RouterProvider router={routers} />
        </AuthProvider>
      </Provider>
    </Suspense>
  );
};

export default App;
