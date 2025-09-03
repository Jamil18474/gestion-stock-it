import React, { useState, useContext } from 'react';
import axios from '../api/axios';
import { useNavigate } from 'react-router-dom';
import Container from '@mui/material/Container';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Alert from '@mui/material/Alert';
import { AuthContext } from '../AuthContext';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const { login } = useContext(AuthContext);
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('/token/', { username, password })
            .then(res => {
                login(res.data.access, { username });
                navigate('/');
            })
            .catch(() => setError('Identifiants invalides'));
    };

    return (
        <Container maxWidth="sm" sx={{ mt: 8 }}>
            <Box sx={{ p: 3, boxShadow: 2, borderRadius: 2, background: '#fff' }}>
                <Typography variant="h5" gutterBottom>Connexion</Typography>
                <form onSubmit={handleSubmit}>
                    <TextField
                        fullWidth label="Nom d'utilisateur"
                        value={username} onChange={e => setUsername(e.target.value)} sx={{ mb: 2 }} required
                    />
                    <TextField
                        fullWidth label="Mot de passe"
                        type="password"
                        value={password} onChange={e => setPassword(e.target.value)} sx={{ mb: 2 }} required
                    />
                    <Button type="submit" variant="contained">Se connecter</Button>
                    {error && <Alert severity="error" sx={{ mt: 2 }}>{error}</Alert>}
                </form>
            </Box>
        </Container>
    );
}

export default Login;