import React, { useContext } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { AuthContext } from '../AuthContext';

function Navbar() {
    const { isAuthenticated, logout, user } = useContext(AuthContext);
    const navigate = useNavigate();

    const handleLogout = () => {
        logout();
        navigate('/login');
    };

    return (
        <Box sx={{ flexGrow: 1 }}>
            <AppBar position="static">
                <Toolbar>
                    <Typography variant="h6" sx={{ flexGrow: 1 }}>
                        Gestion Stock IT
                    </Typography>
                    {isAuthenticated ? (
                        <>
                            <Button color="inherit" component={Link} to="/">Accueil</Button>
                            <Button color="inherit" component={Link} to="/materiels">Matériels</Button>
                            <Button color="inherit" component={Link} to="/categories">Catégories</Button>
                            <Button color="inherit" component={Link} to="/mouvements">Mouvements</Button>
                            <Button color="inherit" component={Link} to="/inventaires">Inventaires</Button>
                            <Typography sx={{ ml: 2, mr: 2 }}>{user?.username}</Typography>
                            <Button color="error" onClick={handleLogout}>Déconnexion</Button>
                        </>
                    ) : (
                        <Button color="inherit" component={Link} to="/login">Connexion</Button>
                    )}
                </Toolbar>
            </AppBar>
        </Box>
    );
}

export default Navbar;