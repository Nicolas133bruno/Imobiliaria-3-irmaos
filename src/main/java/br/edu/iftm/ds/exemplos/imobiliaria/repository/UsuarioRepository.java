package br.edu.iftm.ds.exemplos.imobiliaria.repository;

import br.edu.iftm.ds.exemplos.imobiliaria.domain.Usuario;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.Optional;

public interface UsuarioRepository extends JpaRepository<Usuario, Integer> {
    Optional<Usuario> findByLoginUsu(String loginUsu);
}
