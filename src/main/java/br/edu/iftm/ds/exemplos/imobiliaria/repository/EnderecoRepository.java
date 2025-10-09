package br.edu.iftm.ds.exemplos.imobiliaria.repository;


import br.edu.iftm.ds.exemplos.imobiliaria.domain.Endereco;
import org.springframework.data.jpa.repository.JpaRepository;

public interface EnderecoRepository extends JpaRepository<Endereco, Integer> {
}
