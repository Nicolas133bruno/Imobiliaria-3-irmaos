package br.edu.iftm.ds.exemplos.imobiliaria.Service;

import br.edu.iftm.ds.exemplos.imobiliaria.domain.Usuario;
import br.edu.iftm.ds.exemplos.imobiliaria.repository.UsuarioRepository;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

@Service
public class UsuarioService {

    private final UsuarioRepository userRepo;
    private final BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();

    public UsuarioService(UsuarioRepository userRepo) {
        this.userRepo = userRepo;
    }

    public Usuario save(Usuario u) {
        u.setSenhaUsu(encoder.encode(u.getSenhaUsu()));
        return userRepo.save(u);
    }
}
