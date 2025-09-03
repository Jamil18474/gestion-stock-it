import React, { useContext } from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Login from './pages/Login';
import MaterielList from './pages/MaterielList';
import MaterielForm from './pages/MaterielForm';
import CategorieList from './pages/CategorieList';
import CategorieForm from './pages/CategorieForm';
import MouvementList from './pages/MouvementList';
import MouvementForm from './pages/MouvementForm';
import InventaireList from './pages/InventaireList';
import InventaireForm from './pages/InventaireForm';
import { AuthContext } from './AuthContext';

function PrivateRoute({ children }) {
    const { isAuthenticated } = useContext(AuthContext);
    return isAuthenticated ? children : <Navigate to="/login" />;
}

function AppRoutes() {
    return (
        <Routes>
            <Route path="/" element={<PrivateRoute><Dashboard /></PrivateRoute>} />
            <Route path="/login" element={<Login />} />
            <Route path="/materiels" element={<PrivateRoute><MaterielList /></PrivateRoute>} />
            <Route path="/materiels/add" element={<PrivateRoute><MaterielForm /></PrivateRoute>} />
            <Route path="/materiels/:id/edit" element={<PrivateRoute><MaterielForm /></PrivateRoute>} />
            <Route path="/categories" element={<PrivateRoute><CategorieList /></PrivateRoute>} />
            <Route path="/categories/add" element={<PrivateRoute><CategorieForm /></PrivateRoute>} />
            <Route path="/categories/:id/edit" element={<PrivateRoute><CategorieForm /></PrivateRoute>} />
            <Route path="/mouvements" element={<PrivateRoute><MouvementList /></PrivateRoute>} />
            <Route path="/mouvements/add" element={<PrivateRoute><MouvementForm /></PrivateRoute>} />
            <Route path="/inventaires" element={<PrivateRoute><InventaireList /></PrivateRoute>} />
            <Route path="/inventaires/add" element={<PrivateRoute><InventaireForm /></PrivateRoute>} />
            <Route path="*" element={<Navigate to="/" />} />
        </Routes>
    );
}

export default AppRoutes;