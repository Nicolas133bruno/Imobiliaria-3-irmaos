package br.edu.iftm.ds.exemplos.imobiliaria.config;

import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.filter.OncePerRequestFilter;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import br.edu.iftm.ds.exemplos.imobiliaria.repository.UsuarioRepository;
import java.io.IOException;
import java.util.List;

public class JwtAuthFilter extends OncePerRequestFilter {

    private final JwtUtil jwtUtil;
    private final UsuarioRepository userRepo;

    public JwtAuthFilter(JwtUtil jwtUtil, UsuarioRepository userRepo){
        this.jwtUtil = jwtUtil;
        this.userRepo = userRepo;
    }

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain chain)
            throws ServletException, IOException {

        String header = request.getHeader("Authorization");

        if (header != null && header.startsWith("Bearer ")) {
            String token = header.substring(7);

            if (jwtUtil.validate(token)) {
                String login = jwtUtil.getUsername(token);

                userRepo.findByLoginUsu(login).ifPresent(user -> {
                    String perfil = (user.getPerfil() != null) ? user.getPerfil().getTipo_perf() : "CLIENTE";
                    var auth = new UsernamePasswordAuthenticationToken(
                            login, null,
                            List.of(new SimpleGrantedAuthority("ROLE_" + perfil.toUpperCase()))
                    );
                    SecurityContextHolder.getContext().setAuthentication(auth);
                });
            }
        }

        chain.doFilter(request, response);
    }
}
